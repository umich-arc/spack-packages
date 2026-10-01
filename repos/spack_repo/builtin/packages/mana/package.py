# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mana(Package):
    """MPI-Agnostic, Network-Agnostic transparent checkpoint/restart for MPI.

    MANA builds against the DMTCP revision bundled as a Git submodule.
    """

    homepage = "https://github.com/mpickpt/mana"
    git = "https://github.com/mpickpt/mana.git"

    version("1.4.0", commit="3af4bf549b40ab4a6a4f341eb57ba83c01335261", submodules=True)

    variant("debug", default=False, description="Enable MANA and DMTCP debugging")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("gmake", type="build")
    depends_on("mpi")
    conflicts("^mpich~fortran", msg="MANA builds Fortran MPI wrappers")
    conflicts("^openmpi~fortran", msg="MANA builds Fortran MPI wrappers")
    requires("platform=linux")

    phases = ["configure", "build", "install"]
    patch("arc.patch", when="@1.4.0", sha256="01c566af234146a94f854cdb421b1915d209f7d6546d4dc60945de0a8b55f4f4")

    def setup_build_environment(self, env):
        # Always use the pinned submodule, even when the user has DMTCP loaded.
        env.unset("DMTCP_ROOT")
        env.unset("MANA_ROOT")

    def configure(self, spec, prefix):
        # The checked-in configure scripts are sufficient; no autoreconf needed.
        # MANA rejects the extra options supplied by a generic Autotools builder.
        Executable("./configure")(
            "--prefix={0}".format(prefix),
            "--libdir={0}".format(prefix.lib),
            "--enable-debug" if "+debug" in spec else "--disable-debug",
        )
        # Upstream incorrectly passes CFLAGS (including -std=gnu11) to Fortran.
        filter_file(
            "${MPIFORTRAN} ${CFLAGS}",
            "${MPIFORTRAN} ${FFLAGS}",
            "mpi-proxy-split/mpi-wrappers/Makefile",
            string=True,
        )
        filter_file(
            "FFLAGS = ${CXXFLAGS} @FFLAGS@",
            "FFLAGS = @FFLAGS@",
            "mpi-proxy-split/Makefile_config.in",
            string=True,
        )
        Executable("./config.status")("mpi-proxy-split/Makefile_config")

    @property
    def mpi_make_args(self):
        # Command-line assignments propagate to recursive make invocations and
        # override the hard-coded wrappers in Makefile_config (including Cray).
        mpi = self.spec["mpi"]
        return [
            "CC={0}".format(spack_cc),
            "CXX={0}".format(spack_cxx),
            "MPICC={0}".format(mpi.mpicc),
            "MPICXX={0} -std=c++14".format(mpi.mpicxx),
            "MPIFORTRAN={0}".format(mpi.mpifc),
        ]

    def build(self, spec, prefix):
        # The top-level default target also builds MPI test applications with
        # unbounded parallelism. Build only the runtime and plugin instead.
        make("mana_prereqs", "dmtcp")
        with working_dir("mpi-proxy-split"):
            make("install", *self.mpi_make_args)

    def install(self, spec, prefix):
        with working_dir("dmtcp"):
            make("install")
        # MANA's own install rules only populate the source tree, ignoring
        # prefix/DESTDIR. Preserve its expected bin/ and lib/dmtcp/ layout.
        install_tree("bin", prefix.bin)
        install_tree("lib", prefix.lib)
        mkdirp(prefix.share.man.man1)
        install("manpages/mana.1", prefix.share.man.man1)
        for script in ("mana_launch", "mana_restart", "mana_shadow_mpi_libs.py"):
            filter_file(
                "#!/usr/bin/env python3",
                "#!{0}".format(spec["python"].command.path),
                join_path(prefix.bin, script),
                string=True,
            )
