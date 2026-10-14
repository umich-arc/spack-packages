# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRsample(RPackage):
    """Classes and functions to create and summarize different types of
    resampling objects (e.g. bootstrap, cross-validation)."""

    homepage = "https://rsample.tidymodels.org/"
    cran = "rsample"

    supplier = "Hannah Frick"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("1.3.2", sha256="760aaa8bf61ff4dbeeb7e35cc5892cc77b2262690a5d34eb0e455517d3202ef2")
    version("1.3.1", sha256="6b31fbd90350a809c7ee673d406e19d720becb456ac5146e8b05171171f06430")
    version("1.3.0", sha256="f3f4df79910f13231951ac3b68ffb57092e8a88a92ccc6c11f7948c004aac991")
    version("1.2.1", sha256="e3f437f21ea527d1c9fa344494b4c127254c5c5d87b0b2aecfcbdeea5964edc5")
    version("1.2.0", sha256="e0c9b7060e0037f4213a5faad73f5910cf97bf93ecba93d35301cbc88cf45eed")
    version("1.1.1", sha256="90d2ae86d27a397ba9d8d010e7dea5c7b86fecbec7e9af273db0c2e8c374b8ba")
    version("1.1.0", sha256="4b06c00d766d131cc9b5c1d1c2b94e53034467d6909f692af90932c9630ec6c7")
    version("1.0.0", sha256="c5af8def9912679ff7670d11b2a4dcd945a396d42142aaee62409bd5bafc7758")
    version("0.1.1", sha256="5f10359723a971d1bdf03d74292d1b0c7778d5f8ab9a2559daab6ff78984bc07")
    version("0.1.0", sha256="cb18a182cf2de10fe45bf7db3f54f26fd581b2fdef24c13d43d5a5442ec88803")
    version("0.0.9", sha256="4cb4bc9708c9314aecaad703bae5aeffdd533af0bf1273a05042d647fdd61c0f")
    version("0.0.8", sha256="71e0d1a3852c5a2d8cac7d498878976de6452c4ceb815ec00e7f9166c2ec55df")
    version("0.0.7", sha256="a832e978edde276d79e513bfa75e289c174fc64f76e016bd55716c96017ed068")
    version("0.0.6", sha256="721abefbc213b125a2c1fea6671f6d967d28fb688184aa4ea3fef4b544fe49ed")
    version("0.0.5", sha256="ed6a379f7f334d2eea5dd3100846ca586af7a7f774e93b3f114f33b49a877c52")
    version("0.0.4", sha256="a8671e62293eb134eb39072955b2732462388b2c2fc481aba924be23cb492038")
    version("0.0.3", sha256="c19308b3a859d9029fb754762534218096cd9b890f6c59a8b71aa89563eab4bd")
    version("0.0.2", sha256="aeaab3dc6c407707668610316dee6c8288c403fdbdfcd59d908500c588bf9582")
    version("0.0.1", sha256="a298118c4a22663e52afd4706784b88d15d197cd455e0e082308bf9b3c374bd0")

    with default_args(type=("build", "run")):
        depends_on("r-cli")
        depends_on("r-dplyr@1.1.1:")
        depends_on("r-furrr")
        depends_on("r-generics")
        depends_on("r-glue")
        depends_on("r-lifecycle")
        depends_on("r-pillar")
        depends_on("r-purrr@1.0.0:")
        depends_on("r-rlang@1.1.0:")
        depends_on("r-slider@0.1.5:")
        depends_on("r-tibble")
        depends_on("r-tidyr")
        depends_on("r-tidyselect")
        depends_on("r-vctrs@0.5.0:")
