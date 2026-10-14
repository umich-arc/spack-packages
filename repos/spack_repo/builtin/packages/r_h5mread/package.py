# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RH5mread(RPackage):
    """A fast HDF5 reader"""

    homepage = "A fast HDF5 reader"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/h5mread_1.4.1.tar.gz"
    bioc = "h5mread"

    supplier = "Hervé Pagès"

    maintainers("theAeon")

    license("Artistic-2.0", checked_by="theAeon")

    version("1.4.1", sha256="855891f46162f3ece2917b5b3e601310dc284d4a42e29f5f991cf43961009580")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-rhdf5")
        depends_on("r-biocgenerics")
        depends_on("r-sparsearray")
        depends_on("r-rhdf5filters")
        depends_on("r-s4vectors")
        depends_on("r-iranges")
        depends_on("r-s4arrays")
