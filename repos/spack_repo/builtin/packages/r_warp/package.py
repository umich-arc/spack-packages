# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RWarp(RPackage):
    """Tooling to group dates by a variety of periods including:
    yearly, monthly, by second, by week of the month, and more.
    The groups are defined in such a way that they also represent the distance
    between dates in terms of the period. This extracts valuable information
    that can be used in further calculations that rely on a
    specific temporal spacing between observations."""

    homepage = "https://github.com/DavisVaughan/warp"
    cran = "warp"

    supplier = "Davis Vaughan"

    maintainers("theAeon")

    license("MIT", checked_by="theAeon")

    version("0.2.3", sha256="bdf3404b90ea5d1754242d87512b9d44c9a5825207d0010a956354266bda112a")
    version("0.2.2", sha256="f57b544c75e3a2457a149a5ff0d5835ccfc917f8192440ef44fdf7d952197840")
    version("0.2.1", sha256="020ad590de099661aa62b4d5e51499a2ac91c41c61db2dbc71c3f4a3df2c46be")
    version("0.2.0", sha256="0e0de344f3d711d58e6be2ab47ade1db3b703bf3ca85080b1124c0c25a630a68")
    version("0.1.0", sha256="a23654b5e51dda5f4d19ec613d2ac572dc491cd0582b1c095c4b031852f57599")

    depends_on("c", type="build")
