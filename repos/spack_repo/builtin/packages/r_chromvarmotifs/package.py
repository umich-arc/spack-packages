# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RChromvarmotifs(RPackage):
    """The goal of chromVARmotifs is to make it easy to use several different motif collections in R
    particularly for use with motifmatchr and chromVAR packages. """

    git = "https://github.com/GreenleafLab/chromVARmotifs.git"

    with default_args(get_full_repo=True):
        version("0.2.0", commit="38bed559c1f4770b6c91c80bf3f8ea965da26076")


    depends_on("r-tfbstools", type=("build", "run"))

