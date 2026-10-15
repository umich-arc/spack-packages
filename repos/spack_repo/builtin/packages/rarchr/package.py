# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rarchr(RCollectivePackage):
    """Easily install the ArchR environment"""

    has_code = False
    metalist = {"1.0.3_R4.6.1": [("r", "4.6.1"), ("r-archr", "1.0.3"), ("gsl", "2.8"), ("py-macs2", "2.2.8")]}

    for key, value in metalist.items():
        version(key)
        for pairing in value:
            depends_on(f"{pairing[0]}@{pairing[1]}", when=f"@{key}", type="run")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
