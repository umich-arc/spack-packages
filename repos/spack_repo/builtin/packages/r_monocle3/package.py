# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMonocle3(RPackage):
    """Tools for Single Cell Genomics.

    Monocle 3 is an analysis toolkit for single-cell RNA-Seq experiments. To use this package,
    you will need the R statistical computing environment (version 3.0 or later) and several
    packages available through Bioconductor and CRAN."""

    homepage = "https://github.com/cole-trapnell-lab/monocle3"
    url = "https://github.com/cole-trapnell-lab/monocle3/archive/refs/tags/v1.4.27.tar.gz"

    version("1.4.27", sha256="34618523d3a96557af3e8980f88ddd42df4134ae0f8043d5f9ed44df29716952")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-assertthat@0.2.1:", type=("build", "run"))
    depends_on("r-batchelor", type=("build", "run"))
    depends_on("r-biocgenerics@0.28.0:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-bpcells", type=("build", "run"))
    depends_on("r-delayedarray@0.8.0:", type=("build", "run"))
    depends_on("r-delayedmatrixstats@1.4.0:", type=("build", "run"))
    depends_on("r-digest@0.6.28:", type=("build", "run"))
    depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
    depends_on("r-future@1.23.0:", type=("build", "run"))
    depends_on("r-ggdist@3.3.0:", type=("build", "run"))
    depends_on("r-ggforce@0.4.1:", type=("build", "run"))
    depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
    depends_on("r-ggrastr", type=("build", "run"))
    depends_on("r-ggrepel@0.8.1:", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-igraph@1.5.0:", type=("build", "run"))
    depends_on("r-irlba@2.3.3:", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-lmtest", type=("build", "run"))
    depends_on("r-leidenbase@0.1.25:", type=("build", "run"))
    depends_on("r-limma@3.38.3:", type=("build", "run"))
    depends_on("r-mass@7.3-51.4:", type=("build", "run"))
    depends_on("r-matrix@1.2-17:", type=("build", "run"))
    depends_on("r-openssl", type=("build", "run"))
    depends_on("r-pbapply@1.4-0:", type=("build", "run"))
    depends_on("r-pbmcapply@1.4.1:", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-plotly@4.9.0:", type=("build", "run"))
    depends_on("r-plyr@1.8.4:", type=("build", "run"))
    depends_on("r-proxy@0.4-23:", type=("build", "run"))
    depends_on("r-pscl@1.5.2:", type=("build", "run"))
    depends_on("r-purrr@0.3.2:", type=("build", "run"))
    depends_on("r-rann@2.6.1:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcpp@1.0.1:", type=("build", "run"))
    depends_on("r-rcppannoy", type=("build", "run"))
    depends_on("r-rcpphnsw@0.3.o:", type=("build", "run"))
    depends_on("r-reshape2@1.4.3:", type=("build", "run"))
    depends_on("r-rsample@0.0.5:", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-rtsne@0.15:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-sf", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-slam@0.1-45:", type=("build", "run"))
    depends_on("r-spdep@1.1-2:", type=("build", "run"))
    depends_on("r-speedglm@0.3-2:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.11.5:", type=("build", "run"))
    depends_on("r-uwot@0.1.8:", type=("build", "run"))
    depends_on("r-tibble@2.1.1:", type=("build", "run"))
    depends_on("r-tidyr@0.8.3:", type=("build", "run"))
    depends_on("r-viridis@0.5.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-knitr", type=("build"))
