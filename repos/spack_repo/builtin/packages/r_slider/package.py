# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSlider(RPackage):
    """Provides type-stable rolling window functions over any R data type.
    Cumulative and expanding windows are also supported. For more advanced usage,
    an index can be used as a secondary vector that defines how sliding windows
    are to be created."""

    homepage = "https://github.com/r-lib/slider"
    cran = "slider"

    supplier = "Davis Vaughan"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("0.3.3", sha256="7ad3a7c7ff56c472fcf55a5a9fc8f11879e0d232f8a7a5a736c38b0ecac6f0ac")
    version("0.3.2", sha256="c9304db3f964475053c5795f160c1e278fa572b114f4e7ecf1686a5899dc3619")
    version("0.3.1", sha256="200a26795fadb2058e3976af7a697dde7f120645279cfe2580b8c0d6c0a429b0")
    version("0.3.0", sha256="bc6a17ba5f0b27c8504a1d04992108470f24fd5662fbea14c300ac75fb02fca1")
    version("0.2.2", sha256="a35537604bf7065594e0f23fec403c0272dd992cf92329e2647ceb31d812b3ef")
    version("0.2.1", sha256="1c2f92a1589d69ccd61694701614db2593e5047d1beb738c72c8323c1c8232ca")
    version("0.2.0", sha256="9d631e236438a574926ea0de7677d5bb8c2b6debaf54f28ab0ab1b0141591133")
    version("0.1.5", sha256="93f5801ad81a6e4f7e710666a2ca1530709767d10d171dd6749f91aabae392f4")
    version("0.1.4", sha256="ac8393b3c4d7196f56486fe6631859b13c3d60db5385abee3b10e4e58c1e4a71")
    version("0.1.3", sha256="bf680941527427c0e790f63f51beba121a40acaa9534e185b161a6a8c40ea5e6")
    version("0.1.2", sha256="f80b96800e16ca0b57d596e96c820bedd6fb8bc33bd736801557dfd720de7040")
    version("0.1.1", sha256="f85b4b3f7ea1570c0e57f5f9e8a3fc91086cee1a055883c4fe7983ee153a82ce")
    version("0.1.0", sha256="0450b6a18e3799853d8f23630d68b140e3a73c9a49ea0271e319b366bc122816")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-cli@3.6.1:")
        depends_on("r-rlang@1.1.1:")
        depends_on("r-vctrs@0.6.3:")
        depends_on("r-warp")
