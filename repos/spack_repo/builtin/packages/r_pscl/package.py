# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPscl(RPackage):
    """Bayesian analysis of item-response theory (IRT) models, roll call analysis;
    computing highest density regions; maximum likelihood estimation of
    zero-inflated and hurdle models for count data; goodness-of-fit measures for
    GLMs; data sets used in writing and teaching; seats-votes curves."""

    homepage = "https://github.com/atahk/pscl"
    cran = "pscl"

    supplier = "Simon Jackman"

    maintainers("theAeon")

    license("GPL-2.0-Only", checked_by="theAeon")

    version("1.5.9", sha256="8085ffd1987804793ba44637165fba3e6805aa2f6457f0692b6e641658fe6efe")
    version("1.5.5.1", sha256="611367c3d34c78f2d4db79e630e38d7a5df8296bd7e72d258f6a115fbbe78d5b")
    version("1.5.5", sha256="054c9b88a991abdec3338688f58e81b6ba55f91edb988621864b24fd152fee6f")
    version("1.5.2", sha256="2c9fe648485c6b54c6f95a54b6e00ffe3cf06fa8c5c68f1d669664a7b91a0ede")
    version("1.5.1", sha256="83139144d010997da1bee469ebf4067117239dbb5067c70e8352348e8f2105a4")
    version("1.4.9", sha256="0e3a08a5d1ab73b84e4a3b3bb1893d6bf534eb4e53e5ffe80d3ec341ac91d195")
    version("1.4.8", sha256="7fb5c2860010e056152a3fa3f0f8f23aebf572075698900c15f47ea5df904fc7")
    version("1.4.6", sha256="7ee903692d841251019aa96e782921dd273d1fddecff0db218dd8c47aaad6d8d")
    version("1.04.4", sha256="d63cf4a8a39c97a1edfb310c850a9c96a71323d5d4740e8c9e186176a6c2a856")
    version("1.04.1", sha256="ca77267db42335002edbf3e2fb6fe339a5641c935070ba2d9e6abc1654009138")
    version("1.04", sha256="06ff91fdffe953036412542c70511ee90e221297ee7464504531f7d9b448a448")
    version("1.03.10", sha256="f447d01885dbb1a510dc6087ddf3dfb6ea5d9fec5984dfb6a6cabab50605b0e1")
    version("1.03.6.1", sha256="a21da459cea3e794c21516565ab78aa0be448d5e017c7b5031338aaf419d8052")
    version("1.03.6", sha256="4cfa5b3ae4e46f5c766032c778012f4557aec47e3e46bc2c2dee1bc243e5eaac")
    version("1.03.5", sha256="ac2e095567888d5e89ee0bbb7e3ddf189dfc1520dd3280ac070645c4b7d9c865")
    version("1.03.4", sha256="af64e20f7f7fc186b5d6f2de894e397f50c6d5a62433afca6cee09c20de3bab3")
    version("1.03.3", sha256="7c74c58c8e365fbbd9d88ce749f873c41b903edfb00c8a962fb55369ab8c52d4")
    version("1.03.2", sha256="6f8fddcddc74b25b35ffc06a169ee2d9f11c869f80ac639e6ee65978a28820a7")
    version("1.03", sha256="e56ffb4249ef82bb5655f7b7377fc8c69401e22cb49fa0f692aa00d99710e296")
    version("1.02", sha256="700ab8f82e6926d174cd3cc8fbabd693e8bc34fa7b5ee49c883db51d0d4f9e87")
    version("1.01", sha256="14c191ee9b3286f14bcc5876175c428a2fff7ed6d74711c1bbfb85d283363c85")
    version("1.00", sha256="ad3c20e74c39677fba520675dfdfad50b45bc648c4dabc0389583b05f2787437")
    version("0.97", sha256="0e635c24e2999bae5e177fbbf51e03d8b6668018a1dcdf975c3a1de829a34927")
    version("0.96", sha256="da777aa9201eecc0149528573ff4caba4f011db44c7f9b31e4385e2db87cc8c8")
    version("0.95", sha256="b6624d7228b0db4e51dd7e7d838ad6dea2b5841d2126e781bae39c48dec6806a")
    version("0.94", sha256="905dc2d67462352b687c75a850344a606f9d9b4f5c5810d9df5387a72840f839")
    version("0.92", sha256="20a41d58cb89cb225d3fe0d8093051850bd638e9e3c2a793187112a39c057812")
    version("0.91", sha256="ae984cd941fcbca297336d57356a58f18bd08642e2c4208f59482c1bbec3dd96")
    version("0.75", sha256="f4a7a89e485f7d1f21fa98d68758ab31fda29a339f7e8374d1d347b6edadde55")
    version("0.73", sha256="292bb753c7fac58fa52b90e59d1424e6435683151fdfc998d38d9a15107c4e2e")
    version("0.72", sha256="9557abdb1ae0d0b8c1589e8c29c325eca116a2c2e0ddea19dcb65ecbbe0ad8e5")
    version("0.61", sha256="ffc0b3d3839e7a83bfeb73fe3342b752a4fd912b41903f126e40291e9d419473")
    version("0.60", sha256="c60fb07f9e4619e7d87b4af2c262ae947175c3869e1b5a4d32842b9c65537991")
    version("0.59", sha256="d1779ed713f8fbda1f6a2bd15cc16010bf07ffb1426e140325ad4e4c9a0d9a41")
    version("0.58", sha256="8a668bc877868debca65fe97802383e67fbccd47d0b788d885e77a0ff2060be4")
    version("0.54", sha256="f374686269ca30d49d870f36f54aad1d9170e2dc18c0ecff17ca2fde8c5a4ef8")
    version("0.52", sha256="8ee7c89ea16ca27bcef2b91e350b07e271463218594014c7fd0c4e88fe6bdabd")
    version("0.51", sha256="de56a91a16bdebb2820507b58ea9c0ea93b71c5418dba3f090552a6e6f9f0f1f")
    version("0.5", sha256="65c9e1e23b8e768a4c44c8da72a93ef033249cdbddebd7b5c9f2284916cd82db")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-mass")
