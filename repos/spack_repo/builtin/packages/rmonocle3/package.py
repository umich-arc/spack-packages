# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rmonocle3(RCollectivePackage):
    """Monocle 3 and its R dependencies in one collective library."""

    has_code = False
    version("1.4.27_R4.6.1")

    r_github_dependencies = {"monocle3": "cole-trapnell-lab/monocle3@v1.4.27"}
    r_dependencies = (
        "assertthat",
        "batchelor",
        "BiocGenerics",
        "BiocParallel",
        "DelayedArray",
        "DelayedMatrixStats",
        "digest",
        "dplyr",
        "future",
        "ggdist",
        "ggforce",
        "ggplot2",
        "ggrastr",
        "ggrepel",
        "HDF5Array",
        "igraph",
        "irlba",
        "lme4",
        "lmtest",
        "leidenbase",
        "limma",
        "MASS",
        "Matrix",
        "openssl",
        "pbapply",
        "pbmcapply",
        "pheatmap",
        "plotly",
        "plyr",
        "proxy",
        "pscl",
        "purrr",
        "RANN",
        "RColorBrewer",
        "Rcpp",
        "RcppAnnoy",
        "RcppHNSW",
        "reshape2",
        "rsample",
        "RhpcBLASctl",
        "Rtsne",
        "S4Vectors",
        "sf",
        "shiny",
        "slam",
        "spdep",
        "speedglm",
        "stringr",
        "SummarizedExperiment",
        "uwot",
        "tibble",
        "tidyr",
        "viridis",
        "Biobase",
        "SingleCellExperiment",
        "knitr",
        #"bpcells",
    )
    bioc_version = "3.23"

    depends_on("r@4.6.1", when="@1.4.27_R4.6.1", type=("build", "run"))
    depends_on("gdal")
    depends_on("geos")
    depends_on("proj")
    depends_on("hdf5")
    depends_on("mpi", when="^hdf5+mpi")
    depends_on("pkgconfig", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gdal"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["geos"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["proj"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["hdf5"].prefix.lib)
        if "+mpi" in self.spec["hdf5"]:
            # BPCells uses R's compiler directly. Parallel HDF5's pkg-config
            # flags omit the MPI headers, so provide them to its configure
            # checks and generated C++ Makevars through CFLAGS.
            env.append_flags("CFLAGS", self.spec["mpi"].headers.cpp_flags)
