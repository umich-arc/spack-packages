# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from types import SimpleNamespace

import pytest

from spack_repo.builtin.build_systems.r import RCollectiveBuilder


def build_script(tmp_path, r_dependencies):
    captured = []
    module = SimpleNamespace(
        r_lib_dir=str(tmp_path / "library"), R=lambda *args: captured.extend(args)
    )
    package = SimpleNamespace(
        name="r-test",
        r_dependencies=r_dependencies,
        r_github_dependencies={},
        r_repositories={"CRAN": "https://cloud.r-project.org"},
        bioc_version=None,
        module=module,
    )
    spec = SimpleNamespace(dependencies=lambda **kwargs: [])

    RCollectiveBuilder.install(None, package, spec, str(tmp_path / "prefix"))
    return captured[-1]


def test_r_collective_installs_exact_package_versions(tmp_path):
    script = build_script(
        tmp_path, {"GenomicRanges": "1.42.0", "ggplot2": "3.5.2", "Seurat": None}
    )

    assert "remotes::install_version" in script
    assert '"GenomicRanges" = "1.42.0"' in script
    assert '"ggplot2" = "3.5.2"' in script
    assert 'c("Seurat")' in script
    assert "installed R package version does not match" in script


def test_r_collective_keeps_name_only_declarations(tmp_path):
    script = build_script(tmp_path, ("Seurat",))

    assert 'c("Seurat")' in script
    assert "remotes::install_version" not in script


def test_r_collective_rejects_invalid_pinned_versions(tmp_path):
    with pytest.raises(ValueError, match="invalid exact version"):
        build_script(tmp_path, {"Seurat": "1.0; stop('bad')"})
