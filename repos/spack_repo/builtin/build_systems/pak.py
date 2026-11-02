# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
"""Pak-managed R collections, with Spack-managed native dependencies."""

import json
import os
import re

from spack.package import (
    BuilderWithDefaults,
    HeaderList,
    LibraryList,
    build_system,
    depends_on,
    extends,
    join_path,
    mkdirp,
    register_builder,
)

from .generic import Package


def _string(value):
    # JSON strings are also valid R string literals; never interpolate raw R code.
    return json.dumps(str(value), ensure_ascii=True)


def _vector(values):
    return "c(" + ", ".join(_string(value) for value in values) + ")"


def _named(values):
    return "setNames(" + _vector(values.values()) + ", " + _vector(values) + ")"


def collection_inputs(pkg):
    """Validate declarations before touching the install prefix or network."""
    declared = pkg.r_dependencies
    if isinstance(declared, (tuple, list)):
        if any(not isinstance(name, str) for name in declared):
            raise ValueError("r_dependencies names must be strings")
        if len(set(declared)) != len(declared):
            raise ValueError("duplicate names in r_dependencies")
        declared = dict.fromkeys(declared)
    if not isinstance(declared, dict) or not isinstance(pkg.r_github_dependencies, dict):
        raise ValueError("R dependencies must be a sequence or mapping; GitHub requires a mapping")
    github = pkg.r_github_dependencies
    names = list(declared) + list(github)
    if not names:
        raise ValueError("declare at least one R package")
    if len(set(names)) != len(names):
        raise ValueError("duplicate package in R and GitHub dependencies")
    if any(not isinstance(n, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9.]*", n) for n in names):
        raise ValueError("invalid R package name")
    pinned = {name: version for name, version in declared.items() if version is not None}
    for version in pinned.values():
        if not isinstance(version, str) or not re.fullmatch(r"[0-9]+(?:[.-][0-9]+)*", version):
            raise ValueError("invalid exact version")
    refs = [name if version is None else f"{name}@{version}" for name, version in declared.items()]
    for name, ref in github.items():
        if not isinstance(ref, str) or not re.fullmatch(
            r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:@[A-Za-z0-9._/-]+)?", ref
        ):
            raise ValueError("invalid GitHub reference")
        refs.append(f"{name}=github::{ref}")
    repos = pkg.r_repositories
    if not isinstance(repos, dict) or not repos:
        raise ValueError("configure at least one R repository")
    if any(
        not isinstance(k, str) or not k or not isinstance(v, str)
        or not re.fullmatch(r"https?://[^\s]+", v)
        for k, v in repos.items()
    ):
        raise ValueError("repositories must map names to HTTP(S) URLs")
    if pkg.bioc_version is not None and not re.fullmatch(r"[0-9]+\.[0-9]+", pkg.bioc_version):
        raise ValueError("invalid Bioconductor version")
    return names, pinned, refs, dict(repos)


class PakPackage(Package):
    """An R collection installed by pak into a single prefix.

    Declare R roots in ``r_dependencies`` (names or exact-version mapping),
    and GitHub roots in ``r_github_dependencies`` (R name to owner/repo@ref).
    Only R and native dependencies belong in the Spack DAG. Subclasses must
    declare compilers and native libraries required by their R packages.
    """

    build_system_class = "PakPackage"
    default_buildsystem = "pak"
    build_system("pak")
    has_code = False
    extends("r")
    depends_on("gmake", type="build")

    r_dependencies = ()
    r_github_dependencies = {}
    r_repositories = {"CRAN": "https://cloud.r-project.org"}
    bioc_version = None
    # Optional absolute path, or path relative to stage.source_path (e.g. a resource).
    pak_lockfile = None

    @property
    def r_spec(self):
        return self.spec["r"]

    @property
    def headers(self):
        return HeaderList([])

    @property
    def libs(self):
        return LibraryList([])


@register_builder("pak")
class PakBuilder(BuilderWithDefaults):
    phases = ("install",)

    def install(self, pkg, spec, prefix):
        names, pinned, refs, repos = collection_inputs(pkg)
        source_lock = None
        if pkg.pak_lockfile:
            source_lock = os.path.abspath(join_path(pkg.stage.source_path, pkg.pak_lockfile))
            if not os.path.isfile(source_lock):
                raise ValueError(f"pak lockfile does not exist: {source_lock}")
        library = str(pkg.module.r_lib_dir)
        metadata = join_path(prefix, ".spack-pak")
        lockfile = join_path(metadata, "pkg.lock")
        mkdirp(library, metadata)
        # Load only from the selected interpreter's own base library, before
        # adding the collection library to the search path.
        script = f'''
            library <- {_string(library)}
            lockfile <- {_string(lockfile)}
            repos <- {_named(repos)}
            pak_path <- find.package("pak", lib.loc = .Library, quiet = TRUE)
            if (!length(pak_path)) stop(
                "The selected R installation must provide pak in its base library: ",
                .Library)
            tryCatch(loadNamespace("pak", lib.loc = .Library), error = function(e)
                stop("Cannot load pak from the selected R installation: ",
                     conditionMessage(e)))
            required <- c("lockfile_create", "lockfile_install")
            if (!all(required %in% getNamespaceExports("pak")))
                stop("The selected R installation's pak lacks the required lockfile API")
            writeLines(c(paste0("Version: ", packageVersion("pak", lib.loc = .Library)),
                         paste0("Library: ", .Library), paste0("Package: ", pak_path)),
                       {_string(join_path(metadata, 'pak-info.txt'))})
            Sys.setenv(R_LIBS_USER = library, R_LIBS = library,
                       PKG_SYSREQS = "false", PKG_PLATFORMS = "source",
                       PKG_CACHE_DIR = {_string(join_path(pkg.stage.path, 'pak-cache'))})
            .libPaths(c(library, .Library))
            options(repos = repos, Ncpus = 1L, pkg.sysreqs = FALSE,
                    pkg.platforms = "source")
        '''
        if pkg.bioc_version:
            script += f'\nSys.setenv(R_BIOC_VERSION = {_string(pkg.bioc_version)})\n'
        if source_lock:
            script += f'''
                if (!file.copy({_string(source_lock)}, lockfile, overwrite = TRUE))
                    stop("cannot copy pak lockfile")
            '''
        else:
            script += f'''
                pak::lockfile_create(pkg = {_vector(refs)}, lockfile = lockfile,
                                     lib = NULL, dependencies = NA)
            '''
        script += f'''
            pak::lockfile_install(lockfile = lockfile, lib = library)
            installed <- installed.packages(lib.loc = library)
            missing <- setdiff({_vector(names)}, installed[, "Package"])
            if (length(missing)) stop("missing requested R packages: ",
                                      paste(missing, collapse = ", "))
            pinned <- {_named(pinned)}
            actual <- setNames(installed[, "Version"], installed[, "Package"])
            if (any(actual[names(pinned)] != pinned)) stop("R package version mismatch")
            for (name in {_vector(names)}) loadNamespace(name, lib.loc = library)
            installed <- installed[order(installed[, "Package"]), , drop = FALSE]
            write.table(installed[, c("Package", "Version", "Built"), drop = FALSE],
                        file = {_string(join_path(metadata, 'packages.tsv'))},
                        sep = "\\t", quote = FALSE, row.names = FALSE)
            writeLines(capture.output(sessionInfo()),
                       {_string(join_path(metadata, 'session-info.txt'))})
        '''
        script_path = join_path(metadata, "install.R")
        with open(script_path, "w", encoding="utf-8") as stream:
            stream.write(script)
        pkg.module.R("--vanilla", "--slave", "-f", script_path)
