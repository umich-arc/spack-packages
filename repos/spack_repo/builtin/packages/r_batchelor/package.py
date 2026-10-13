# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBatchelor(RPackage):
    """Implements a variety of methods for batch correction of single-cell (RNA sequencing) data.
    This includes methods based on detecting mutually nearest neighbors,
    as well as several efficient variants of linear regression of the log-expression values.
    Functions are also provided to perform global rescaling to remove
    differences in depth between batches, and to perform a principal components analysis
    that is robust to differences in the numbers of cells across batches."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/batchelor.html"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/batchelor_1.28.0.tar.gz"
    bioc = "batchelor"

    supplier = "Aaron Lun"

    maintainers("theAeon")

    license("GPL-3.0-only", checked_by="theAeon")

    version("1.28.0", sha256="21914b11692f95631d1ce2ad4c963caa00ad4eef163d1502faeadbf9f9959978")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-biocneighbors", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-sparsearray", type=("build", "run"))
    depends_on("r-delayedarray@0.31.5:", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-residualmatrix", type=("build", "run"))
    depends_on("r-beachmat", type=("build", "run"))
