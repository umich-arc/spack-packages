# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBiocmake(RPackage):
    """Manages the installation of CMake for building Bioconductor packages."""

    homepage = "https://github.com/LTLA/biocmake"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/biocmake_1.4.0.tar.gz"
    bioc = "biocmake"

    supplier = "Aaron Lun"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.4.0", sha256="158c59fd65dca9b5e74e5c4f32a1fbe161e080d1278d99816a802980c653210d")

    with default_args(type=("build", "run")):
        depends_on("r-dir-expiry")
