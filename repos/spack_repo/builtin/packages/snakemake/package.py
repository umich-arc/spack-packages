# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.uv import UvPackage

from spack.package import *


class Snakemake(UvPackage):
    """Workflow management system to create reproducible and scalable data analyses."""

    homepage = "https://snakemake.readthedocs.io/en"
    pypi = "snakemake/snakemake-9.6.3.tar.gz"
    maintainers("marcusboden", "w8jcik")

    license("MIT")

    version("9.14.0")
    depends_on("python@3.8:", type=("build", "run"))

    @property
    def python_dependencies(self):
        return {"snakemake": str(self.version)}
