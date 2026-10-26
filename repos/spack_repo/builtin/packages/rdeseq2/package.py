# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rdeseq2(RCollectivePackage):
    """Estimate variance-mean dependence in count data from high-throughput
    sequencing assays and test for differential expression based on a model
    using the negative binomial distribution.
    """

    bioc = "DESeq2"
    bioc_version = "3.23"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/DESeq2_1.52.0.tar.gz"

    license("LGPL-3.0-or-later")

    version("1.52.0")
    r_dependencies = ("DESeq2",)
    bioc_version = "3.23"

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@4.6:", type=("build", "run"))
