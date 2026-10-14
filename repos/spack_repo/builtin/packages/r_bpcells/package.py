# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage, RBuilder

from spack.package import *

class RSubBuilder(RBuilder):
    '''Install the package starting in the subdirectory "r"'''
    def install(self, pkg, spec, prefix):
        """Installs an R package."""
        mkdirp(pkg.module.r_lib_dir)

        config_args = self.configure_args()
        config_vars = self.configure_vars()

        args = ["--vanilla", "CMD", "INSTALL"]

        if config_args:
            args.append(f"--configure-args={' '.join(config_args)}")

        if config_vars:
            args.append(f"--configure-vars={' '.join(config_vars)}")

        args.extend([f"--library={pkg.module.r_lib_dir}", self.stage.source_path + "/r"])

        pkg.module.R(*args)



class RBpcells(RPackage):
    """Efficient operations for single cell ATAC-seq fragments and
    RNA counts matrices. Interoperable with standard file formats, and introduces
    efficient bit-packed formats that allow large storage savings and increased
    read speeds."""

    GenericBuilder = RSubBuilder

    homepage = "https://bnprks.github.io/BPCells/"
    url = "https://github.com/bnprks/BPCells/archive/refs/tags/v0.3.1.tar.gz"

    supplier = "Benjamin Parks"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("0.3.1", sha256="76f55ec77c9784d4b4ad80e7a0fc5c8139fa8101857edd5772ece70cbd8ae584")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("hdf5~mpi")

    with default_args(type=("build", "run")):
        depends_on("r-magrittr")
        depends_on("r-matrix")
        depends_on("r-rcpp")
        depends_on("r-rlang")
        depends_on("r-vctrs")
        depends_on("r-lifecycle")
        depends_on("r-stringr")
        depends_on("r-tibble")
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-tidyr")
        depends_on("r-readr")
        depends_on("r-ggplot2@3.4.0:")
        depends_on("r-scales")
        depends_on("r-patchwork")
        depends_on("r-scattermore")
        depends_on("r-ggrepel")
        depends_on("r-rcolorbrewer")
        depends_on("r-hexbin")
        depends_on("r-rcppeigen")

