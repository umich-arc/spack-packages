# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rarchr(RCollectivePackage):
    """Easily install the ArchR environment"""

    has_code = False
    version("1.0.3_R4.6.1")

    r_github_dependencies = {"ArchR": "GreenleafLab/ArchR@v1.0.3"}
    depends_on("r@4.6.1", when="@1.0.3_R4.6.1", type=("build", "run"))
    depends_on("gsl@2.8", when="@1.0.3_R4.6.1", type=("build", "run"))
    depends_on("py-macs2@2.2.8", when="@1.0.3_R4.6.1", type="run")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gsl"].prefix.lib)
