# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RChromvar(RPackage):
    """Chromatin Variation Across Regions"""

    homepage = "https://bioconductor.org/packages/release/bioc/html/chromVAR.html"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/chromVAR_1.34.1.tar.gz"
    bioc = "chromVAR"

    supplier = "Alicia Schep"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.34.1", sha256="6fe247d12c57a19619d3216a81f263c8bd08245bc392f6c023caae128373a615")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-iranges")
        depends_on("r-seqinfo")
        depends_on("r-genomicranges")
        depends_on("r-ggplot2")
        depends_on("r-nabor")
        depends_on("r-biocparallel")
        depends_on("r-biocgenerics")
        depends_on("r-biostrings")
        depends_on("r-pwalign")
        depends_on("r-tfbstools")
        depends_on("r-rsamtools")
        depends_on("r-s4vectors")
        depends_on("r-rcpp")
        depends_on("r-plotly")
        depends_on("r-shiny")
        depends_on("r-miniui")
        depends_on("r-dt")
        depends_on("r-rtsne")
        depends_on("r-matrix")
        depends_on("r-summarizedexperiment")
        depends_on("r-rcolorbrewer")
        depends_on("r-bsgenome")
        depends_on("r-rcpparmadillo")
