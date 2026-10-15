# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RChipenrichData(RPackage):
    """Companion package to chipenrich"""

    homepage = "https://bioconductor.org/packages/3.23/data/experiment/html/chipenrich.data.html"
    url = "https://bioconductor.org/packages/3.23/data/experiment/src/contrib/chipenrich.data_2.36.0.tar.gz"
    bioc = "chipenrich.data"

    supplier = "Kai Wang"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("2.36.0", sha256="231999c156b12cf97f69efc1a46821c8c2b9bce6683dfc4c1d302e80ac0d96a8")

    with default_args(type=("build", "run")):
        depends_on("r-annotationdbi")
        depends_on("r-biocgenerics")
        depends_on("r-genomicranges")
        depends_on("r-genomeinfodb")
        depends_on("r-iranges")
        depends_on("r-readr")
        depends_on("r-rtracklayer")
        depends_on("r-s4vectors")
