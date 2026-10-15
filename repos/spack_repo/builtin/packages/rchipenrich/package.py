# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rchipenrich(RCollectivePackage):
    """Easily Install and Load chipenrich"""

    license("MIT")
    has_code = False
    metalist = {"2.36.0_R4.6.1": [("r", "4.6.1"), ("r-chipenrich", "2.36.0")]}

    for key, value in metalist.items():
        version(key)
        for pairing in value:
            depends_on(f"{pairing[0]}@{pairing[1]}", when=f"@{key}", type="run")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
