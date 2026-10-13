# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGgdist(RPackage):
    """Provides primitives for visualizing distributions using 'ggplot2' that are particularly
    tuned for visualizing uncertainty in either a frequentist or Bayesian mode. Both analytical
    distributions (such as frequentist confidence distributions or Bayesian priors) and distributions
    represented as samples (such as bootstrap distributions or Bayesian posterior samples) are easily
    visualized. Visualization primitives include but are not limited to: points with multiple
    uncertainty intervals, eye plots (Spiegelhalter D., 1999) dot plots
    <https://ideas.repec.org/a/bla/jorssa/v162y1999i1p45-58.html>, density plots, gradient plots,
    (Wilkinson L., 1999) <doi:10.1080/00031305.1999.10474474>, quantile dot plots
    (Kay M., Kola T., Hullman J., Munson S., 2016) <doi:10.1145/2858036.2858558>,
    complementary cumulative distribution function barplots
    (Fernandes M., Walls L., Munson S., Hullman J., Kay M., 2018)
    <doi:10.1145/3173574.3173718>, and fit curves with multiple uncertainty ribbons."""

    homepage = "https://github.com/mjskay/ggdist/"
    cran = "ggdist"

    supplier = "Matthew Kay"

    maintainers("theAeon")

    license("GPL-3.0-or-later", checked_by="theAeon")

    version("3.3.3", sha256="f35563b2ab9799f47db9ae90da3434cc0fa436426e979d0f143308510dfd3673")
    version("3.3.2", sha256="f6563091cb7ca48b4fb415740a60113be6aac541616f5025110364e12cbe83f1")
    version("3.3.1", sha256="6705e8a252701bc162bbbe26f7cbb3e95e93a11af6288456ab711f5d0c0df929")
    version("3.3.0", sha256="1441a6dae5bc4b084a741a6f8782a13235171013cc028bf1d694662e4e5a252c")
    version("3.2.1", sha256="76016ad99e049fdb5be5f93c431733a3c1911ac737930b4deda1648e0af3e228")
    version("3.2.0", sha256="09c989d9ebb282d6eaae37f68a8c98abce61d9788527e691ed2ebe42da111e46")
    version("3.1.1", sha256="d92882b947e8575ecd1aba9117aaf4aca87d90d39af15612af48ff37beb2ed9c")
    version("3.1.0", sha256="bd898f839a678fd75dea86a7920d593cf03651528ebd13a35bd90586763e32fd")
    version("3.0.1", sha256="caa918f4d4cfbb09415c951cf598cea50bae60a7a70507dc64697a206f1c0b3d")
    version("3.0.0", sha256="a921a6965b59ec1226ea75f5db9aa6d303c78f7767ecc9bc1bc784ce9fc23323")
    version("2.4.1", sha256="1dfadc2f37ae9cfa81cdcb7706b1234242a08147e455c6731f502e65f9ca682d")
    version("2.4.0", sha256="56d03e95788d784d1c9505e7f4e008bb33a231defdb610ae1d10e250e5271c55")
    version("2.3.0", sha256="10389c31e22b3ff5fa4dad2aa3f7af270891e56748f283280f8e677a839255d3")
    version("2.2.0", sha256="03856440b52400c4fa03bfe0a6ea403c6f453ed6772087ac200c80f8896336b3")
    version("2.1.1", sha256="287ba57c9d8f99d18779eb54961d55bf910697803188da6e29c2c79844909284")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-ggplot2@3.5.0:")
        depends_on("r-scales")
        depends_on("r-rlang@0.3.0:")
        depends_on("r-cli")
        depends_on("r-tibble")
        depends_on("r-vctrs")
        depends_on("r-withr")
        depends_on("r-glue")
        depends_on("r-gtable")
        depends_on("r-distributional@0.3.2:")
        depends_on("r-numderiv")
        depends_on("r-quadprog")
