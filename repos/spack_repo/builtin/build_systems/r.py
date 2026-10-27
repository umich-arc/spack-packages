# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import json
import re
from typing import Dict, List, Optional, Tuple, Union

import spack.llnl.util.tty as tty
from spack.package import join_path

from spack.package import (
    ClassProperty,
    classproperty,
    depends_on,
    extends,
    mkdirp,
    register_builder,
    BuilderWithDefaults,
    Spec,
    Prefix,
    build_system,
    when,
    HeaderList,
    LibraryList,
)

from .generic import GenericBuilder, Package


class RBuilder(GenericBuilder):
    """The R builder provides a single phase that can be overridden:

        1. :py:meth:`~.RBuilder.install`

    It has sensible defaults, and for many packages the only thing
    necessary will be to add dependencies.
    """

    #: Names associated with package methods in the old build-system format
    package_methods: Tuple[str, ...] = (
        "configure_args",
        "configure_vars",
    ) + GenericBuilder.package_methods

    def configure_args(self):
        """Arguments to pass to install via ``--configure-args``."""
        return []

    def configure_vars(self):
        """Arguments to pass to install via ``--configure-vars``."""
        return []

    def install(self, pkg, spec, prefix):
        """Installs an R package."""
        mkdirp(pkg.module.r_lib_dir)

        config_args = self.configure_args()
        config_vars = self.configure_vars()

        args = ["--vanilla", "CMD", "INSTALL"]

        if config_args:
            args.append(f"--configure-args={' '.join(config_args)}")

        if config_vars:
            args.append(f"--configure-vars={' '.join(config_vars)}")

        args.extend([f"--library={pkg.module.r_lib_dir}", self.stage.source_path])

        pkg.module.R(*args)


def _homepage(cls: "RPackage") -> Optional[str]:
    if cls.cran:
        return f"https://cloud.r-project.org/package={cls.cran}"
    elif cls.bioc:
        return f"https://bioconductor.org/packages/{cls.bioc}"
    return None


def _urls(cls: "RPackage") -> List[str]:
    if cls.cran:
        return [
            f"https://cran.r-project.org/src/contrib/{cls.cran}_{str(list(cls.versions)[0])}.tar.gz",
            f"https://cran.r-project.org/src/contrib/Archive/{cls.cran}/{cls.cran}_{str(list(cls.versions)[0])}.tar.gz",
        ]
    return []


def _list_url(cls: "RPackage") -> Optional[str]:
    if cls.cran:
        return f"https://cran.r-project.org/src/contrib/Archive/{cls.cran}/"
    return None


def _git(cls: "RPackage") -> Optional[str]:
    if cls.bioc:
        return f"https://git.bioconductor.org/packages/{cls.bioc}"
    return None


class RPackage(Package):
    """Specialized class for packages that are built using R.

    For more information on the R build system, see:
    https://stat.ethz.ch/R-manual/R-devel/library/utils/html/INSTALL.html
    """

    # package attributes that can be expanded to set the homepage, url,
    # list_url, and git values
    # For CRAN packages
    cran: Optional[str] = None

    # For Bioconductor packages
    bioc: Optional[str] = None

    GenericBuilder = RBuilder

    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = "RPackage"

    extends("r")

    # needed for packages that need compiling
    depends_on("gmake", type="build", when="%c")
    depends_on("gmake", type="build", when="%cxx")
    depends_on("gmake", type="build", when="%fortran")

    homepage: ClassProperty[Optional[str]] = classproperty(_homepage)
    urls: ClassProperty[List[str]] = classproperty(_urls)
    list_url: ClassProperty[Optional[str]] = classproperty(_list_url)
    git: ClassProperty[Optional[str]] = classproperty(_git)


@register_builder("r_collective")
class RCollectiveBuilder(BuilderWithDefaults):
    """Install R packages and their dependencies into one collective prefix."""

    phases = ("install",)

    def install(self, pkg, spec, prefix):
        declared_dependencies = pkg.r_dependencies
        if isinstance(declared_dependencies, dict):
            package_versions = dict(declared_dependencies)
        elif isinstance(declared_dependencies, (tuple, list)):
            if len(set(declared_dependencies)) != len(declared_dependencies):
                raise ValueError(f"{pkg.name} has duplicate names in r_dependencies")
            package_versions = {name: None for name in declared_dependencies}
        else:
            raise ValueError(
                f"{pkg.name} r_dependencies must be a sequence of names or a "
                "package-name-to-version mapping"
            )

        github_dependencies = dict(pkg.r_github_dependencies)

        if not package_versions and not github_dependencies:
            legacy_packages = []
            legacy_github_dependencies = {}
            for dep in spec.dependencies(deptype=("build", "run")):
                if not dep.name.startswith("r-"):
                    continue
                source = str(getattr(dep.package, "url", "") or "")
                github = re.fullmatch(
                    r"https?://github\.com/([^/]+)/([^/]+)/archive/refs/tags/([^/]+)\.tar\.gz",
                    source,
                )
                if github:
                    legacy_github_dependencies[dep.name[2:]] = (
                        f"{github.group(1)}/{github.group(2)}@{github.group(3)}"
                    )
                else:
                    legacy_packages.append(dep.name[2:])

            if legacy_packages or legacy_github_dependencies:
                tty.warn(
                    f"{pkg.name} still declares R packages as Spack dependencies; "
                    "move them to r_dependencies to remove them from the Spack DAG"
                )
                package_versions = {name: None for name in sorted(legacy_packages)}
                github_dependencies = legacy_github_dependencies
            else:
                raise ValueError(f"{pkg.name} must declare R packages in r_dependencies")

        packages = tuple(package_versions)
        if any(not re.fullmatch(r"[A-Za-z][A-Za-z0-9.]*", name) for name in packages):
            raise ValueError(f"{pkg.name} has an invalid R package name in r_dependencies")
        if any(
            version is not None
            and (
                not isinstance(version, str)
                or not re.fullmatch(r"[0-9]+(?:[.-][0-9]+)*", version)
            )
            for version in package_versions.values()
        ):
            raise ValueError(
                f"{pkg.name} has an invalid exact version in r_dependencies; "
                "versions must contain only numeric components separated by '.' or '-'"
            )
        if set(packages).intersection(github_dependencies):
            raise ValueError(f"{pkg.name} declares the same package in both R dependency lists")
        if any(
            not re.fullmatch(r"[A-Za-z][A-Za-z0-9.]*", name) for name in github_dependencies
        ):
            raise ValueError(f"{pkg.name} has an invalid package name in r_github_dependencies")
        if any(
            not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:@[A-Za-z0-9._/-]+)?", repo)
            for repo in github_dependencies.values()
        ):
            raise ValueError(f"{pkg.name} has an invalid GitHub package in r_github_dependencies")

        repositories = dict(pkg.r_repositories)
        if pkg.bioc_version:
            bioc = f"https://bioconductor.org/packages/{pkg.bioc_version}"
            repositories = {
                "BioCsoft": f"{bioc}/bioc",
                "BioCann": f"{bioc}/data/annotation",
                "BioCexp": f"{bioc}/data/experiment",
                "BioCworkflows": f"{bioc}/workflows",
                **repositories,
            }
        if not repositories:
            raise ValueError(f"{pkg.name} must configure at least one R repository")

        library = pkg.module.r_lib_dir
        metadata = join_path(prefix, ".spack-r-collective")
        manifest = join_path(metadata, "packages.tsv")
        mkdirp(library)
        mkdirp(metadata)

        unpinned_packages = tuple(
            name for name, version in package_versions.items() if version is None
        )
        unpinned_package_vector = ", ".join(json.dumps(name) for name in unpinned_packages)
        pinned_package_versions = {
            name: version for name, version in package_versions.items() if version is not None
        }
        pinned_package_vector = ", ".join(
            f"{json.dumps(name)} = {json.dumps(version)}"
            for name, version in pinned_package_versions.items()
        )
        repository_vector = ", ".join(
            f"{json.dumps(name)} = {json.dumps(url)}" for name, url in repositories.items()
        )
        install_script = ""
        if unpinned_packages:
            install_script += f"""
                install.packages(
                    c({unpinned_package_vector}),
                    lib = library,
                    repos = repos,
                    dependencies = c("Depends", "Imports", "LinkingTo"),
                    Ncpus = 1L
                )
            """
        if pinned_package_versions or github_dependencies:
            install_script += """
                install.packages("remotes", lib = library, repos = repos)
                .libPaths(c(library, .libPaths()))
            """
        if pinned_package_versions:
            install_script += f"""
                pinned_packages <- c({pinned_package_vector})
                for (package in names(pinned_packages)) {{
                    remotes::install_version(
                        package = package,
                        version = unname(pinned_packages[[package]]),
                        lib = library,
                        repos = repos,
                        dependencies = c("Depends", "Imports", "LinkingTo"),
                        upgrade = "never",
                        build_vignettes = FALSE
                    )
                }}
            """
        if github_dependencies:
            github_vector = ", ".join(
                json.dumps(repo) for repo in github_dependencies.values()
            )
            install_script += f"""
                install.packages("BiocManager", lib = library, repos = repos)
                repos <- c(BiocManager::repositories(), repos)
                options(repos = repos)
                .libPaths(c(library, .libPaths()))
                remotes::install_github(
                    c({github_vector}),
                    lib = library,
                    dependencies = c("Depends", "Imports", "LinkingTo"),
                    upgrade = "never",
                    build_vignettes = FALSE
                )
            """
        requested_vector = ", ".join(
            [json.dumps(name) for name in packages]
            + [json.dumps(name) for name in github_dependencies]
        )
        r_script = f"""
            library <- {json.dumps(library)}
            packages <- c({requested_vector})
            pinned_packages <- c({pinned_package_vector})
            repos <- c({repository_vector})
            dir.create(library, recursive = TRUE, showWarnings = FALSE)
            Sys.setenv(R_LIBS_USER = library)
            .libPaths(c(library, .libPaths()))
            options(repos = repos)
            {install_script}
            installed <- installed.packages(lib.loc = library)
            missing <- setdiff(packages, installed[, "Package"])
            if (length(missing)) {{
                stop("failed to install requested R packages: ",
                     paste(missing, collapse = ", "))
            }}
            installed_versions <- setNames(installed[, "Version"], installed[, "Package"])
            mismatched <- names(pinned_packages)[
                installed_versions[names(pinned_packages)] != pinned_packages
            ]
            if (length(mismatched)) {{
                stop("installed R package version does not match the requested version: ",
                     paste(
                         paste0(mismatched, " (requested ", pinned_packages[mismatched],
                                ", installed ", installed_versions[mismatched], ")"),
                         collapse = ", "
                     ))
            }}
            write.table(
                installed[, c("Package", "Version")],
                file = {json.dumps(manifest)},
                sep = "\\t",
                quote = FALSE,
                row.names = FALSE
            )
        """
        tty.info(
            f"Installing R packages {', '.join(packages + tuple(github_dependencies))} into {library}"
        )
        pkg.module.R("--vanilla", "--slave", "-e", r_script)


class RCollectivePackage(RPackage):
    """An R package environment with all R dependencies in one prefix.

    Declare R package names in ``r_dependencies`` as a sequence, or use a
    package-name-to-exact-version mapping to pin selected versions, for example
    ``{"GenomicRanges": "1.42.0", "ggplot2": "3.5.2"}``. These packages and their
    Depends, Imports, and LinkingTo dependencies are installed into a single
    library in this package's prefix. Use ``depends_on`` only for the R
    interpreter and non-R build or runtime dependencies. GitHub packages may
    be declared as package-name-to-repository entries in
    ``r_github_dependencies``.
    """

    build_system_class = "RCollectivePackage"
    default_buildsystem = "r_collective"
    build_system("r_collective")

    has_code = False
    r_dependencies: Union[Tuple[str, ...], Dict[str, Optional[str]]] = ()
    r_github_dependencies: Dict[str, str] = {}
    r_repositories: Dict[str, str] = {"CRAN": "https://cloud.r-project.org"}
    bioc_version: Optional[str] = None

    with when("build_system=r_collective"):
        extends("r")

    @property
    def r_spec(self) -> Spec:
        """R interpreter used by this collective."""
        r, *_ = self.spec.dependencies("r")
        return r

    @property
    def headers(self) -> HeaderList:
        return HeaderList([])

    @property
    def libs(self) -> LibraryList:
        return LibraryList([])
