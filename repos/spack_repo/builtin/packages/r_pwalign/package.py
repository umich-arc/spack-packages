# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPwalign(RPackage):
    """Perform pairwise sequence alignments"""

    homepage = "https://bioconductor.org/packages/pwalign"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/pwalign_1.8.0.tar.gz"
    bioc = "pwalign"


    supplier = "Hervé Pagès"
    maintainers("theAeon")

    license("Artistic-2.0", checked_by="theAeon")

    version("1.8.0", sha256="54d97ddcba175658ca44bc813f458f7b376257cdac1341a62940a2d895062485")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-s4vectors")
        depends_on("r-iranges")
        depends_on("r-biostrings@2.71.5:")
