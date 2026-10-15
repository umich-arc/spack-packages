# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RHarmony(RPackage):
    """Implementation of the Harmony algorithm for single cell integration, described in Patikas, Yao, et al"""

    homepage = "https://pati-ni.github.io/harmony/"
    cran = "harmony"

    supplier = "Broad Institute"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("2.0.5", sha256="907a3c4808656f6bad5a8e314704f92a0cb159ae298390315d5c73794d9a0c6c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-dplyr")
        depends_on("r-cowplot")
        depends_on("r-ggplot2")
        depends_on("r-matrix")
        depends_on("r-tibble")
        depends_on("r-rlang")
        depends_on("r-rhpcblasctl")
        depends_on("r-cli")
        depends_on("r-rcpparmadillo")
        depends_on("r-rcppprogress")
