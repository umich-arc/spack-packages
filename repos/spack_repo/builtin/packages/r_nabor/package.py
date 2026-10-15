# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RNabor(RPackage):
    """An R wrapper for 'libnabo', an exact or approximate k nearest neighbour
    library which is optimised for low dimensional spaces (e.g. 3D). '"""

    homepage = "https://github.com/jefferis/nabor"
    cran = "nabor"

    supplier = "Gregory Jefferis"

    maintainers("theAeon")

    license("BSD-3-Clause", checked_by="theAeon")

    version("0.5.0", sha256="47938dcc987279281c13abfd667660bf1b3b76af116136a27eb066ee1a4b43da")
    version("0.4.7", sha256="a6fe3bdec991a48fcbd3124bbd9012d68951f9e74df6fded8b99766ff0b6bd99")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-rcpp@0.11.2:")
        depends_on("r-rcppeigen@0.3.2.2.0:")
        depends_on("r-bh@1.54.0-4:")
