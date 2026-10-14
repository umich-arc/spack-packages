# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGlmgampoi(RPackage):
    """Fit a Gamma-Poisson Generalized Linear Model"""

    homepage = "https://github.com/const-ae/glmGamPoi"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/glmGamPoi_1.24.0.tar.gz"
    bioc = "glmGamPoi"

    supplier = "Constantin Ahlmann-Eltze"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.24.0", sha256="faf17f91e8e84a6cb455c7588df352f24da2f5a07e7d4ab8a3b654889a1e7492")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-rcpp")
        depends_on("r-rcpparmadillo")
        depends_on("r-beachmat")
        depends_on("r-assorthead")
        depends_on("r-delayedmatrixstats")
        depends_on("r-matrixstats")
        depends_on("r-matrixgenerics")
        depends_on("r-sparsearray@1.5.21:")
        depends_on("r-s4vectors")
        depends_on("r-delayedarray")
        depends_on("r-hdf5array")
        depends_on("r-matrix")
        depends_on("r-summarizedexperiment")
        depends_on("r-singlecellexperiment")
        depends_on("r-biocgenerics")
        depends_on("r-rlang")
        depends_on("r-vctrs")
