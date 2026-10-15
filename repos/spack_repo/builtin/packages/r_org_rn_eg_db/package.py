# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class ROrgRnEgDb(RPackage):
    """Genome wide annotation for Rat"""

    homepage = "https://bioconductor.org/packages/3.23/data/annotation/html/org.Rn.eg.db.html"
    url = "https://bioconductor.org/packages/3.23/data/annotation/src/contrib/org.Rn.eg.db_3.23.0.tar.gz"
    bioc = "org.Rn.eg.db"

    maintainers("theAeon")

    license("Artistic-2.0", checked_by="theAeon")

    version("3.23.0", sha256="2fb0c72f8da59a80cb760590e3b5261c9a79890ee4170da13e44a83017d22fc8")

    with default_args(type=("build", "run")):
        depends_on("r-annotationdbi")
