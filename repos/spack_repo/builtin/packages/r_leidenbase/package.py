# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RLeidenbase(RPackage):
    """An R to C/C++ interface that runs the Leiden community
    detection algorithm to find a basic partition (). It runs the
    equivalent of the 'leidenalg' find_partition() function, which is
    given in the 'leidenalg' distribution file
    'leiden/src/functions.py'. This package includes the
    required source code files from the official 'leidenalg'
    distribution and functions from the R 'igraph'
    package.  The 'leidenalg' distribution is available from
    <https://github.com/vtraag/leidenalg/>
    and the R 'igraph' package is available from
    <https://igraph.org/r/>.
    The Leiden algorithm is described in the article by
    Traag et al. (2019) <doi:10.1038/s41598-019-41695-z>.
    Leidenbase includes code from the packages:
       igraph version 0.9.8 with license GPL (>= 2),
       leidenalg version 0.8.10 with license GPL 3."""

    homepage = "https://github.com/cole-trapnell-lab/leidenbase"
    cran = "leidenbase"

    supplier = "Brent Ewing"

    maintainers("theAeon")

    license("GPL-3.0-Only", checked_by="theAeon")

    version("0.1.37", sha256="3035f98daae57ec4e3d6cea97794a874cc3bf50b6bea0219e35eff5b0d696761")
    version("0.1.36", sha256="e53d949a26a5c6ffa7e4bc302b672516d35ba465611f6dd02e3ccdeda857b8a2")
    version("0.1.35", sha256="0339e1fa967b6decc222b0aaecd8190c5697458c2a7034b0348490cdfc9f807d")
    version("0.1.32", sha256="22770b3d1f6a0e78a9de1adadd0aa6a4e2d8a47defaf75c83751885aeefdc490")
    version("0.1.31", sha256="cd0a825fa44485e957847321c02b32ac5205675e56df00cd883ea50b9aab23e1")
    version("0.1.30", sha256="5415a5a87665fe03dc439c29abb8fd5aed0a536b806e8e12b04fafcdc511e2cb")
    version("0.1.27", sha256="c3168a68828aacfcf78c6c39415b4771f084c5b5c3c9b2e226dcb8cf909d7b27")
    version("0.1.25", sha256="9eaeb33597fb2926b0ec1723dec44a17e1a08919eac873fa48a6cd697036d5d3")
    version("0.1.23", sha256="cc4510c50c6a85159ae430338018a3858c1a486d745f0206f9ec3ec101f128c9")
    version("0.1.18", sha256="b56fa823bce97c98e886896111041d50b12c1d1aad4ec01a829851a537d0dbfd")
    version("0.1.17", sha256="9adda0c6d7210f8c9ca8348e5c27ed18e6daef24305b57b032be78de65af4cb1")
    version("0.1.14", sha256="78df2fc0804f2f3a68d775039cc4483ed22f34bb8f9b1a4f52b1ffcb6877207d")
    version("0.1.12", sha256="f8e7038fb5d531509e347ab437f424047027853a558c83187290f67547dd1397")
    version("0.1.11", sha256="3627c35bc192f43d2ba09aebbb54f2871efefed5978e19492fb75b6df25d12aa")
    version("0.1.9", sha256="6f96eb78d1dc642381a0867229736a18735279bfa1adfb5a41e8fd33aec41678")
    version("0.1.8", sha256="8ec2fa7d53f4acc367e3a669cee75b7ca04abfd975331e738cd839fce84b1a45")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-igraph@0.9.0:")
