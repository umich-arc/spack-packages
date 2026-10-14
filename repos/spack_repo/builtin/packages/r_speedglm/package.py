# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSpeedglm(RPackage):
    """Fitting Linear and Generalized Linear Models to Large Data Sets.

    Fitting linear models and generalized linear models to large data sets by
    updating algorithms."""

    cran = "speedglm"

    license("GPL-2.0-or-later")

    version("0.3-5", sha256="f8663677c10ff324c5639402060ddd2b1a1e917445cb0f8f84e146b85e82bb4b")

    depends_on("r-biglm", type=("build", "run"), when="@0.3-5:")
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
