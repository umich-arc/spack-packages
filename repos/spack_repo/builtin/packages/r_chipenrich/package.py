# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RChipenrich(RPackage):
    """Gene Set Enrichment For ChIP-seq Peak Data"""

    homepage = "https://bioconductor.org/packages/release/bioc/html/chipenrich.html"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/chipenrich_2.36.0.tar.gz"
    bioc = "chipenrich"

    supplier = "Kai Wang"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("2.36.0", sha256="14b0c148628d7299110735272705e453f226272d8ed1246f5b6bb7aa1f614052")

    with default_args(type=("build", "run")):
        depends_on("r-annotationdbi")
        depends_on("r-biocgenerics")
        depends_on("r-chipenrich-data")
        depends_on("r-seqinfo")
        depends_on("r-genomicranges")
        depends_on("r-iranges")
        depends_on("r-lattice")
        depends_on("r-latticeextra")
        depends_on("r-mass")
        depends_on("r-mgcv")
        depends_on("r-org-dm-eg-db")
        depends_on("r-org-dr-eg-db")
        depends_on("r-org-hs-eg-db")
        depends_on("r-org-mm-eg-db")
        depends_on("r-org-rn-eg-db")
        depends_on("r-plyr")
        depends_on("r-rms")
        depends_on("r-rtracklayer")
        depends_on("r-s4vectors@0.23.10:")
        depends_on("r-stringr")
