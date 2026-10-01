# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Tomviz(CMakePackage):
    """Tomviz provides visualization and analysis of volumetric tomography data."""

    homepage = "https://github.com/OpenChemistry/tomviz"
    git = "https://github.com/OpenChemistry/tomviz.git"

    license("BSD-3-Clause")

    version("3.0.0", tag="3.0.0", submodules=True)

    generator("ninja")
    requires("%gcc", msg="This starter recipe uses GCC")
    requires("build_type=Release")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("paraview@6: +qt +python")
    depends_on("python@3: +shared", type=("build", "link", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
    depends_on("qt-base@6: +gui +network")
    depends_on("qt-5compat@6:")
    depends_on("qt-svg@6:")
    depends_on("qt-tools@6: +assistant")
    depends_on("freetype")

    patch("pybind11_ctvlib_vtk-eigen.patch", when="@3.0.0")

    def cmake_args(self):
        spec = self.spec
        # Read Python from ParaView's dependency DAG, including its exact hash.
        python = spec["paraview"]["python"]
        if spec["python"].dag_hash() != python.dag_hash():
            raise InstallError("Tomviz and ParaView must use the same concrete Python spec")

        return [
            self.define(
                "TOMVIZ_PARAVIEW_INCLUDE_DIR",
                join_path(
                    spec["paraview"].prefix.include,
                    "paraview-{0}".format(spec["paraview"].version.up_to(2)),
                ),
            ),
            self.define("Qt6Core5Compat_DIR", spec["qt-5compat"].prefix.lib.cmake.Qt6Core5Compat),
            self.define("Qt6Svg_DIR", spec["qt-svg"].prefix.lib.cmake.Qt6Svg),
            self.define("Qt6Help_DIR", spec["qt-tools"].prefix.lib.cmake.Qt6Help),
            self.define("freetype_DIR", spec["freetype"].prefix),
            self.define("Python3_ROOT_DIR", python.prefix),
            self.define("Python3_EXECUTABLE", python.command.path),
            self.define("Python3_INCLUDE_DIR", python.headers.directories[0]),
            self.define("Python3_LIBRARY", python.libs[0]),
            self.define("ENABLE_TESTING", self.run_tests),
            self.define("TOMVIZ_DOWNLOAD_WEB", False),
        ]

    @run_after("install")
    def install_python_dependencies(self):
        python = self.spec["paraview"]["python"]
        destination = join_path(self.prefix.lib, "site-packages")
        mkdirp(destination)
        for dependency, module in (("py-scipy", "scipy"), ("py-pygments", "pygments")):
            dep = self.spec[dependency]
            if dep["python"].dag_hash() != python.dag_hash():
                raise InstallError("{0} must use ParaView's concrete Python spec".format(dependency))
            found = False
            for relative_dir in sorted({python.package.purelib, python.package.platlib}):
                source = join_path(dep.prefix, relative_dir)
                if os.path.isdir(source):
                    # Include metadata and any sibling shared-library directories.
                    install_tree(source, destination)
                    found = found or os.path.isdir(join_path(source, module))
            if not found:
                raise InstallError("Could not locate the {0} Python package".format(module))

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", join_path(self.prefix.lib, "site-packages"))
