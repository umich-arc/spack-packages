# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path
from types import SimpleNamespace

import pytest

from spack_repo.builtin.build_systems.pak import PakBuilder, collection_inputs


def package(tmp_path, **kwargs):
    values = dict(
        r_dependencies={"tidyverse": "2.0.0"}, r_github_dependencies={},
        r_repositories={"CRAN": "https://cloud.r-project.org"},
        bioc_version=None, pak_lockfile=None,
        stage=SimpleNamespace(path=str(tmp_path), source_path=str(tmp_path)),
        module=SimpleNamespace(r_lib_dir=str(tmp_path / "library")),
    )
    values.update(kwargs)
    return SimpleNamespace(**values)


@pytest.mark.parametrize("values", [
    {"r_dependencies": ["x", "x"]},
    {"r_dependencies": "tidyverse"},
    {"r_dependencies": {"bad-name": None}},
    {"r_dependencies": {"x": "1.0;stop()"}},
    {"r_dependencies": ()},
    {"r_github_dependencies": {"tidyverse": "org/repo"}},
    {"r_github_dependencies": {"x": "org/repo;stop()"}},
    {"r_repositories": {}},
    {"r_repositories": {"CRAN": "file:///tmp/repo"}},
    {"bioc_version": "3.20;stop()"},
])
def test_invalid_declarations(tmp_path, values):
    with pytest.raises(ValueError):
        collection_inputs(package(tmp_path, **values))


def test_reference_translation(tmp_path):
    names, pins, refs, repos = collection_inputs(package(
        tmp_path, r_dependencies={"ggplot2": "3.5.2", "cli": None},
        r_github_dependencies={"other": "org/repo@abc123"},
    ))
    assert names == ["ggplot2", "cli", "other"]
    assert pins == {"ggplot2": "3.5.2"}
    assert refs == ["ggplot2@3.5.2", "cli", "other=github::org/repo@abc123"]


def test_install_and_replay(tmp_path):
    pkg = package(tmp_path)
    calls = []
    pkg.module.R = lambda *args: calls.append(args)
    PakBuilder.install(None, pkg, None, str(tmp_path / "prefix"))
    script = Path(calls[0][-1]).read_text()
    assert calls[0][:3] == ("--vanilla", "--slave", "-f")
    assert 'pkg = c("tidyverse@2.0.0")' in script
    assert 'lib = NULL, dependencies = NA' in script
    assert 'PKG_SYSREQS = "false"' in script
    assert 'PKG_PLATFORMS = "source"' in script
    assert 'pak::lockfile_install' in script
    assert 'loadNamespace(name, lib.loc = library)' in script
    assert 'packages.tsv' in script
    assert 'loadNamespace("pak", lib.loc = .Library)' in script
    assert 'pak-info.txt' in script
    assert 'must provide pak in its base library' in script
    assert 'install.packages(' not in script
    assert 'bootstrap' not in script
    assert script.index('loadNamespace("pak"') < script.index('.libPaths(')
    pkg.pak_lockfile = "input.lock"
    (tmp_path / "input.lock").write_text("{}")
    PakBuilder.install(None, pkg, None, str(tmp_path / "prefix"))
    script = Path(calls[-1][-1]).read_text()
    assert "file.copy" in script
    assert "pak::lockfile_create" not in script


def test_missing_lockfile_fails_before_install(tmp_path):
    pkg = package(tmp_path, pak_lockfile="absent.lock")
    with pytest.raises(ValueError, match="does not exist"):
        PakBuilder.install(None, pkg, None, str(tmp_path / "prefix"))
    assert not (tmp_path / "library").exists()
