# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRhpcblasctl(RPackage):
    """Control the number of threads on 'BLAS'
    (Aka 'GotoBLAS', 'OpenBLAS', 'ACML', 'BLIS' and 'MKL').
    And possible to control the number of threads in 'OpenMP'.
    Get a number of logical cores and physical cores if feasible."""

    homepage = "https://prs.ism.ac.jp/~nakama/Rhpc/"
    cran = "RhpcBLASctl"

    supplier = "Ei-ji Nakama"

    maintainers("theAeon")

    license("AGPL-3.0-Only", checked_by="theAeon")

    version("0.23-42", sha256="5c889d5b69e264060b9f1f0383c447f594855b8afc15b7d76d39e4d62b946615")
    version("0.21-247.1", sha256="5be55fd5ddd8173167a48b9f072835a34062ad0268308f2b3fbd1781a5c99769")
    version("0.21-247", sha256="629f5145c47e8e481d8f513a9841ee600d91246593b5ffef07aa1b39af334724")
    version("0.20-137", sha256="db02cbdad32fc54bc60bb27baf0799e919c09c09710c33bf72c741f93421616f")
    version("0.20-17", sha256="f7bdd665901fd0162fa78e4e093446532305b314f1334e7d3e5d974c97018c47")
    version("0.18-205", sha256="b7b1406baacc00f4f1bfceaadc2c1e10326f7f5786928dee79e1e6ed0c1242d3")
    version("0.18-185", sha256="f8ce733fd77cd14854fde1ad5f5d0625124de5e0ae4fe3adb31aea4663062569")
    version("0.18-12", sha256="63894e0dea03701767a522498496972694e3480606adc5fbd8711c684ebc1e93")
    version("0.15-148", sha256="6cdf583499e0561ba3871bd5e5c4b1275fbfc477e7f9b69aca4ebdf41df559b1")
    version("0.14-256", sha256="a3635475b88207148b9c7c30225b716d892a6fd55da2b42c6e9c272320e735e9")
    version("0.14-72", sha256="16dd7ab153bb3c0acbf22ec90febd836802f88a18cf24070b4ce42be296a2710")
    version("0.14-71", sha256="030c9174792504a3e936de8fc23afbf23651652b57f3056aa286f05ad350ae31")
    version("0.13-344.02", sha256="fb97784c3d9677036fee5de8eacc6446daf56631fa9d933ec6fcd21b525caa83")
    version("0.13-343.05", sha256="d962a66884f34c1690605e64452a9ecd53ac7e5c7ac642fca1a5a09198353db2")
    version("0.13-331.21", sha256="a46c0d382e874897d955d9417c437ceb1d44c630bff31aca2693e807b3f0013e")

    depends_on("c", type="build")
