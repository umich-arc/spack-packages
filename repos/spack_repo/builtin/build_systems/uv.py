# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
"""Uv-managed Python collections with Spack-managed native dependencies."""

import os
import re
import shutil

from spack.package import (
    BuilderWithDefaults,
    Executable,
    HeaderList,
    LibraryList,
    build_system,
    depends_on,
    extends,
    join_path,
    mkdirp,
    register_builder,
    when,
)

from .generic import Package


def collection_inputs(pkg):
    """Validate roots before touching the prefix or network."""
    declared = pkg.python_dependencies
    if isinstance(declared, (tuple, list)):
        if any(not isinstance(name, str) for name in declared):
            raise ValueError("python_dependencies names must be strings")
        if len(set(declared)) != len(declared):
            raise ValueError("duplicate Python package")
        declared = dict.fromkeys(declared)
    if not isinstance(declared, dict) or not declared:
        raise ValueError("declare Python dependencies as a nonempty sequence or mapping")
    normalized = set()
    requirements = []
    for name, version in declared.items():
        if not isinstance(name, str) or not re.fullmatch(
            r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?", name
        ):
            raise ValueError("invalid Python distribution name")
        canonical = re.sub(r"[-_.]+", "-", name).lower()
        if canonical in normalized:
            raise ValueError("duplicate Python package")
        normalized.add(canonical)
        if version is not None and (
            not isinstance(version, str)
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.!+_-]*", version)
        ):
            raise ValueError("invalid exact Python version")
        requirements.append(name if version is None else f"{name}=={version}")
    if not isinstance(pkg.python_index_url, str) or not re.fullmatch(
        r"https?://[^\s]+", pkg.python_index_url
    ):
        raise ValueError("python_index_url must be an HTTP(S) URL")
    return dict(declared), requirements


class UvPackage(Package):
    """Install Python roots and their transitive dependencies as one collection.

    Subclasses declare Python roots in ``python_dependencies`` and all necessary
    compilers and native libraries as Spack dependencies.
    """

    build_system_class = "UvPackage"
    default_buildsystem = "uv"
    build_system("uv")
    has_code = False
    with when("build_system=uv"):
        extends("python")
        depends_on("python@3.8:", type=("build", "run"))
        depends_on("py-uv@0.6:", type="build")

    python_dependencies = ()
    python_index_url = "https://pypi.org/simple"
    # Hashed requirements.txt, absolute or relative to stage.source_path; not uv.lock.
    uv_lockfile = None

    @property
    def headers(self):
        return HeaderList([])

    @property
    def libs(self):
        return LibraryList([])


@register_builder("uv")
class UvBuilder(BuilderWithDefaults):
    phases = ("install",)

    def install(self, pkg, spec, prefix):
        roots, requirements = collection_inputs(pkg)
        source_lock = None
        if pkg.uv_lockfile:
            source_lock = os.path.abspath(join_path(pkg.stage.source_path, pkg.uv_lockfile))
            if not os.path.isfile(source_lock):
                raise ValueError(f"uv lockfile does not exist: {source_lock}")
        metadata = join_path(prefix, ".spack-uv")
        mkdirp(metadata)
        lockfile = join_path(metadata, "requirements.txt")
        inputs = join_path(metadata, "requirements.in")
        with open(inputs, "w", encoding="utf-8") as stream:
            stream.write("\n".join(requirements) + "\n")
        python = spec["python"].command
        uv = Executable(join_path(spec["py-uv"].prefix.bin, "uv"))
        common = [
            "--no-config", "--no-managed-python", "--no-python-downloads",
            "--cache-dir", join_path(pkg.stage.path, "uv-cache"),
        ]
        with open(join_path(metadata, "uv-info.txt"), "w", encoding="utf-8") as stream:
            stream.write(uv("--version", output=str))
        if source_lock:
            shutil.copyfile(source_lock, lockfile)
        else:
            uv(*common, "pip", "compile", inputs, "--python", python.path,
               "--default-index", pkg.python_index_url, "--generate-hashes",
               "--output-file", lockfile)
        # Always supply both interpreter and destination. Never mutate Python's prefix.
        uv(*common, "pip", "sync", lockfile, "--python", python.path,
           "--prefix", str(prefix), "--default-index", pkg.python_index_url,
           "--require-hashes", "--link-mode", "copy")
        paths = list(dict.fromkeys(
            join_path(prefix, path)
            for path in (spec["python"].package.purelib, spec["python"].package.platlib)
        ))
        script = f'''
import importlib.metadata as metadata
import re
import sys
sys.path[:0] = {paths!r}
normalize = lambda name: re.sub(r"[-_.]+", "-", name).lower()
installed = {{normalize(d.metadata["Name"]): d.version
             for d in metadata.distributions(path={paths!r})}}
roots = {roots!r}
for name, version in roots.items():
    actual = installed.get(normalize(name))
    if actual is None:
        raise RuntimeError("missing requested Python distribution: " + name)
    if version is not None and actual != version:
        raise RuntimeError("Python distribution version mismatch: " + name)
with open({join_path(metadata, 'packages.json')!r}, "w") as stream:
    import json
    json.dump(installed, stream, indent=2, sort_keys=True)
'''
        script_path = join_path(metadata, "verify.py")
        with open(script_path, "w", encoding="utf-8") as stream:
            stream.write(script)
        python("-I", script_path)
