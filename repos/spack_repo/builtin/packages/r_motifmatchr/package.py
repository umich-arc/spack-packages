# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMotifmatchr(RPackage):
    """Fast Motif Matching in R"""

    homepage = "https://bioconductor.org/packages/release/bioc/html/motifmatchr.html"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/motifmatchr_1.34.0.tar.gz"
    bioc = "motifmatchr"

    supplier = "Alicia Schep"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("1.34.0", sha256="e944ecacdc7515ee1b927a1597337ad254e88b20b145618d6d385cffa022ed76")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-matrix")
        depends_on("r-rcpp")
        depends_on("r-tfbstools")
        depends_on("r-biostrings")
        depends_on("r-bsgenome")
        depends_on("r-s4vectors")
        depends_on("r-summarizedexperiment")
        depends_on("r-genomicranges")
        depends_on("r-iranges")
        depends_on("r-rsamtools")
        depends_on("r-seqinfo")
