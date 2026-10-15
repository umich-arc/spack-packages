# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)



from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RArchr(RPackage):
    """Analyzing single-cell regulatory chromatin in R."""

    homepage = "https://www.archrproject.com/"
    url = "https://github.com/GreenleafLab/ArchR/archive/refs/tags/v1.0.3.tar.gz"

    supplier = "Ryan Corces"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.0.3", sha256="9e3c5f07b599ff806c6f2a74ec619b0847e69cb3e96dc29fa1304f2a381620e4")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-biostrings")
        depends_on("r-cairo")
        depends_on("r-chromvar")
        depends_on("r-chromvarmotifs")
        depends_on("r-complexheatmap")
        depends_on("r-data-table")
        depends_on("r-devtools")
        depends_on("r-genomicranges")
        depends_on("r-ggplot2")
        depends_on("r-ggrepel")
        depends_on("r-gridextra")
        depends_on("r-gtable")
        depends_on("r-gtools")
        depends_on("r-harmony")
        depends_on("r-magrittr")
        depends_on("r-matrix")
        depends_on("r-matrixstats")
        depends_on("r-motifmatchr")
        depends_on("r-nabor")
        depends_on("r-plyr")
        depends_on("r-presto")
        depends_on("r-rcpp@0.12.16:")
        depends_on("r-rcpparmadillo")
        depends_on("r-rhdf5")
        depends_on("r-rsamtools")
        depends_on("r-s4vectors@0.9.25:")
        depends_on("r-seurat")
        depends_on("r-seuratobject")
        depends_on("r-shiny")
        depends_on("r-shinythemes")
        depends_on("r-rhandsontable")
        depends_on("r-sparsematrixstats")
        depends_on("r-stringr")
        depends_on("r-summarizedexperiment")
        depends_on("r-uwot")

