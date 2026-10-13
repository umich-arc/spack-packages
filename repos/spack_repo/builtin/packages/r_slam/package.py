# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSlam(RPackage):
    """Data structures and algorithms for sparse arrays and matrices,
    based on index arrays and simple triplet representations, respectively."""

    homepage = "https://cran.r-project.org/web/packages/slam/index.html"
    cran = "slam"

    supplier = "Kurt Hornik"

    maintainers("theAeon")

    license("GPL-2.0-Only", checked_by="theAeon")

    version("0.1-56", sha256="1a83e06ba3ad9b0b67a489b69fe6599a5b76fe5eac498f2ee68c1381e6daa682")
    version("0.1-55", sha256="0fb8450d002ba79855063300941e830133a1880011d926e644aa639dbde91c03")
    version("0.1-54", sha256="f9ad6f46954d33fe79a5f3bb064a2378f603314cf8b4457951009615a737340f")
    version("0.1-53", sha256="026e6d15243f2dd47e34767aa9e8a55b5c6484f7004e9edbeb51673b9a452d72")
    version("0.1-52", sha256="c383e603583d7c29e7a755a292748f670cb145d146514bd7dba1066e87994126")
    version("0.1-51", sha256="06305e3169d5929467872b40df784c3157c068a6844fd1316156e20be91d5506")
    version("0.1-50", sha256="7899bf3266c204ecccefc1878f96940b117d4503af128f4fbc50fc409163f8bd")
    version("0.1-49", sha256="4800a0fd3102319d13cd1f739f2cd785c8acca4a803e62f22ffb94beb0b39010")
    version("0.1-48", sha256="0a0b32d35fd6b8d1ac021b1358e73d32ab942d274a84fbba732d6c02efdcfade")
    version("0.1-47", sha256="696356a68aa92059fa794444faa4c1775193c723a262a5f75de3c3c3047fcf89")
    version("0.1-46", sha256="0b64989a639b196b6f217b301a8a233cefa66296112efdcad09ec76a4e5f10c6")
    version("0.1-45", sha256="84ab3919c7dbac41d97d076787feacfd6861f669aa2842879dffb46ed4467277")
    version("0.1-44", sha256="638085dc05c7509edc9f84e0aaa66381297bf6a0387a0c7e18099c16a729c986")
    version("0.1-43", sha256="b0c866cc529eb7b8c560ec3e945294e924cf934af6346a72ef4e3df6ecc7c443")
    version("0.1-42", sha256="7206b0189544c9878b83005f80f89626cc2c53cfe3e640aeaa9c3da1f07675df")
    version("0.1-40", sha256="afaca1d4712aa977028215d968c71c20c7de5663b2ce51cc217091af91c625b6")
    version("0.1-39", sha256="9452c64ee8b381be616b6a291c0de3b56d75e7c37bcb6afec0877a31924d36f9")
    version("0.1-38", sha256="d08b5aba75df0331dc731f18c6da2dee7d1c88640d4ba1d4983cd41ec3030e82")
    version("0.1-37", sha256="50e3212cd6784be21d737d2b5b42680c90f555715bb807cb7429013d7630f828")
    version("0.1-35", sha256="da30cd0df4643711177338a0c25e474d8a9a25ce120f5582fbc05d39812271a5")
    version("0.1-34", sha256="3d6e6a3f35d7803a9fd53e6bc5011973699ac1bf4996a77ea1b0e28352d4fb63")
    version("0.1-32", sha256="4d9dff04b30cba7ce48fcf0d2f8c38151dd8235e46171e78917512c99b190600")
    version("0.1-31", sha256="f8770d5416b630bbf57961c537336972d47caec1803532c170a5cb50fbd935f1")
    version("0.1-30", sha256="a8dc50d33395332e6cd9ef4bc7cd03ab780137ab2110742a1d312819b01ebf0a")
    version("0.1-29", sha256="f7a95762b80d6cf668c32658af0feb738fb14e1469800b593a46d9c00dab6366")
    version("0.1-28", sha256="75d04b15ff44c69138a2eddc724775638bdc699b85a9ec32818127b11e6fc942")
    version("0.1-27", sha256="5e7f7b5685ebb99d0fc7e0d9f0ec2fbb8124a557f2198f7b23f4b17c10377a2e")
    version("0.1-26", sha256="e109146528160cc830003cb95b534c2c643fbae2b27c0c8cd18fa1531be3b5b0")
    version("0.1-25", sha256="133affbc3a89af7ad4300310b8795dfefa2c9a202fea6718452b8cf04b06b223")
    version("0.1-24", sha256="32f4f04b8eff68f8cddf6510d4eb79d32cbbe51130d2a2c3901190dc514bac7a")
    version("0.1-23", sha256="c16679909645fff0633730cfef86d7f0f80b26d29b0976ca86fd64e39d41ead9")
    version("0.1-22", sha256="a16d5f6c70b5a61d028f0816aaf6972a4079c78c986b50136a8dac3061e74ce1")
    version("0.1-21", sha256="f6bce950eb19be0b8f0600a70225adb8bb9c66ee804b463c869c32567577be4e")
    version("0.1-20", sha256="e36885671d277894824fd8ad80d5b288db3da0ef886539453fa474a9330f00f1")
    version("0.1-18", sha256="9934206e9d75caf05713ff403973aef0b3abb7519989818fca4222ff7259e3cd")
    version("0.1-17", sha256="5e35df85b1fc0e0ad60253d9181a31e6592e8dc4e22b8fc2f087a6d574b0f288")
    version("0.1-16", sha256="42ea4599a8714601da786289df5cb9570a195f082b39fd649fc7b9340bcaf2cc")
    version("0.1-15", sha256="266ab1eab6dd185d7269e14784b8af31c168e3bdaa429527d121e11541606563")
    version("0.1-14", sha256="eb3d32f2828fda91e6204f4fa9fba8c72e2300abcfafa64e2feb3e7421d115a1")
    version("0.1-13", sha256="9256f94af2332f72d3cdaffcc971ae4d971ab9e7976f84d55e560f16105afecf")
    version("0.1-12", sha256="069e92a5240dbe684f06ed7406ae6445b7ba7b9235b8dce88ba849f5dd48c3f8")
    version("0.1-11", sha256="09ddbf442493fa114f70159a9e1ff8db21600b8615564e146ea46932a165d2b1")
    version("0.1-10", sha256="3b53c9218ee7cce893b7e74e5c382c40934bae5f4d878e15601d40350facca7b")
    version("0.1-9", sha256="98a96677696809a082008ff0b05ec8895addee6a0c500e959bc18849a71a3162")
    version("0.1-7", sha256="88efe6022e383db4ba5e9e3bac6325b176f51af6713b808c519d4aed4dd11ebe")
    version("0.1-6", sha256="2f504fe4d382cb63040816f9939099d5e7fe2a6958165dab2a0a4ba534e29516")
    version("0.1-5", sha256="fec1e11154d1af898bac0f698dc4b8d6e576a19444b58b89746014dac4e2751e")
    version("0.1-4", sha256="be47b599639f2ec317bf48831bf329f46ab60e81338bca4fbe97210a0d62d29e")
    version("0.1-3", sha256="05ad1d7c4729f733699b2b25eb916c68655a93dce75bb17504c0e2f73527e0ef")
    version("0.1-2", sha256="5d21af20d38fa2e86da94a50e54a3af181f8893da5f45f4835d0d069f3dae891")
    version("0.1-1", sha256="3b880bae79f45b5d93b2a3adc571ddb4803e109181ff3aab20c02bcf23390ff6")
    version("0.1", sha256="20d8f9bb8a43636a2c4df6b7ffdf6006bfc6a0c45d9a01c76204fcbceb1791e6")

    depends_on("c", type="build")
