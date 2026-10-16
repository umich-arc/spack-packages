# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPresto(RPackage):
    """Fast differential expression and marker discovery for single-cell data."""

    homepage = "https://immunogenomics.github.io/presto/"
    url = "https://github.com/immunogenomics/presto/archive/refs/tags/v1.1.0.tar.gz"

    supplier = "Broad Institute"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("1.1.0", sha256="0ba5da8f0db70825b7ba865d202a0851fa411d02291b31af59137c991afe5d38")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-rcpp")
        depends_on("r-data-table")
        depends_on("r-dplyr")
        depends_on("r-tidyr")
        depends_on("r-purrr")
        depends_on("r-tibble")
        depends_on("r-matrix")
        depends_on("r-rlang")
        depends_on("r-rcpparmadillo")
