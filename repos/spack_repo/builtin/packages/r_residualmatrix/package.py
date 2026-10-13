# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RResidualmatrix(RPackage):
    """Provides delayed computation of a matrix of residuals after fitting a
    linear model to each column of an input matrix. Also supports partial
    computation of residuals where selected factors are to be preserved in the
    output matrix. Implements a number of efficient methods for operating on
    the delayed matrix of residuals, most notably matrix multiplication
    and calculation of row/column sums or means."""

    homepage = "https://github.com/LTLA/ResidualMatrix"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/ResidualMatrix_1.22.0.tar.gz"
    bioc = "ResidualMatrix"

    supplier = "Aaron Lun"

    maintainers("theAeon")

    license("GPL-3.0-only", checked_by="theAeon")

    version("1.22.0", sha256="3d9246e8f710cc399081bf3b93390db2088327f27fa643c145df9308ded958ed")

    with default_args(type=("build", "run")):
        depends_on("r-delayedarray")
        depends_on("r-s4vectors")
        depends_on("r-matrix")
