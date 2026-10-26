# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rchipenrich(RCollectivePackage):
    """Easily Install and Load chipenrich"""

    license("MIT")
    has_code = False
    version("2.36.0_R4.6.1")
    r_dependencies = ("chipenrich",)
    bioc_version = "3.23"
    depends_on("r@4.6.1", when="@2.36.0_R4.6.1", type=("build", "run"))

    depends_on("c", type="build")
    depends_on("cxx", type="build")
