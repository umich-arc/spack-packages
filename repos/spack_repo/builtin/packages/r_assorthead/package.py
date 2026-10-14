# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAssorthead(RPackage):
    """Vendors an assortment of useful header-only C++ libraries."""

    homepage = "https://github.com/LTLA/assorthead"
    url = "https://bioconductor.org/packages/3.23/bioc/src/contrib/assorthead_1.6.4.tar.gz"
    bioc = "assorthead"

    supplier = "Aaron Lun"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.6.4", sha256="a0ef3e48a205c6e70294dda8c113eda0e349db546946a5581c71e84b0d67444d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
