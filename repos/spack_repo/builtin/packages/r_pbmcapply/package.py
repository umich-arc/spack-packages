# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPbmcapply(RPackage):
    """A light-weight package helps you track and visualize the progress of parallel version
    of vectorized R functions (mc*apply). Parallelization (mc.core > 1) works only
    on *nix (Linux, Unix such as macOS) system due to the lack of fork() functionality, which is
    essential for mc*apply, on Windows."""

    homepage = "https://github.com/kvnkuang/pbmcapply"
    cran = "pbmcapply"

    supplier = "Kevin Kuang"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.5.1", sha256="7ffc2854a384962f0dd523aa9ef33ce8fc290997206b71b840a49049d87112dd")
    version("1.5.0", sha256="df52ed585c0b32ac6180616efd94cd75dd7c5621f5398c0861db2f7b317ba844")
    version("1.4.1", sha256="aa19eeb458f5204cddc88757f71c165ee14b0b5868d20b9b7bac52215b7e7318")
    version("1.3.1", sha256="753c7037d330a8f9e32207bffa0479b7c9bf77537afa5e110511c2aba7be5501")
    version("1.3.0", sha256="65fc806bbe86cd63843f00b3ccd1eadc15473442659df0dd7f0f50afd82350ed")
    version("1.2.5", sha256="b64099b56974330fead9c19bd2d623c2bb76c288d88718e8640767724d0fdc2e")
    version("1.2.4", sha256="04f8ed5f151dfdfb83baefde0605222932c1384cc72d03a08b672d9bbca40072")
    version("1.2.3", sha256="ef61f0aed354c605aa90a4f01c982cf59c086c1d9e1030cad12b6e241f3b4f83")
    version("1.2.2", sha256="e83304ec87fadd8a821bcad2e7f28ea3ab9c51d10985853e35e7d6c2afe8f016")
    version("1.2.1", sha256="8a21dd1aef63fae0a2f45c802023866a9e11fcac82567a32023423bae18d97b6")
    version("1.2.0", sha256="b4d3e03256c20a5be113b7f0ffa999ba24fc4f3537a4b4555a62fa110c69b2a9")
    version("1.1.3", sha256="fa78f1821a900c6b50c03fd6824374c74b3a58cdb1c84c78012d543db2c4d7b2")
    version("1.1.2", sha256="cae176bd7e30d0d1770bbbed2df187d49f4d2397ddf39833a3b52a67a7f9ccc3")
    version("1.1.1", sha256="62c7d8c42c3d564fcb05c124a40d12e700a17a65b789ff4a0f70bb17a84e856e")
    version("1.1.0", sha256="2ca7991d903bb24cba1f106f25585d294a961f9ed0eed9d095f3fc1bd23c2df4")
    version("1.0.0", sha256="fdb8a5e3e1ccaa5c5123cce63b0b3a8c07c0958bcb8075b2c36b2c845ab5cef1")

    depends_on("c", type="build")
