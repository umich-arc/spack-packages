# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class ROrgDmEgDb(RPackage):
    """Genome wide annotation for Fly"""

    homepage = "https://bioconductor.org/packages/3.23/data/annotation/html/org.Dm.eg.db.html"
    url = "https://bioconductor.org/packages/3.23/data/annotation/src/contrib/org.Dm.eg.db_3.22.0.tar.gz"
    bioc = "org.Dm.eg.db"

    maintainers("theAeon")

    license("Artistic-2.0", checked_by="theAeon")

    version("3.22.0", sha256="057f346226b4b3dbdbf840bcddf75f393dcb3162615d70fa79d1e14f408851dc")

    with default_args(type=("build", "run")):
        depends_on("r-annotationdbi")

