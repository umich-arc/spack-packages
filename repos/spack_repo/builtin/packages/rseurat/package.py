# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rseurat(RCollectivePackage):
    """Easily Install and Load the Seurat.

    Seurat is a single cell analysis package for R."""

    license("MIT")
    has_code = False
    version("5.5.1_R4.6.1")
    r_dependencies = ("Seurat",)
    depends_on("r@4.6.1", when="@5.5.1_R4.6.1", type=("build", "run"))

    depends_on("c", type="build")
    depends_on("cxx", type="build")
