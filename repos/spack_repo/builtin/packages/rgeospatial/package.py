# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RCollectivePackage

from spack.package import *


class Rgeospatial(RCollectivePackage):
    """Easily Install and Load Geospatial Packages in R.

    This package provides an easy way to install and load multiple geospatial
    packages in R, ensuring that all necessary dependencies are correctly
    configured."""

    has_code = False
    version("1.5-18_R4.6.1")
    version("1.5-18_R4.5.3")
    r_dependencies = (
        "geosphere",
        "chromote",
        "leafem",
        "leaflet",
        "satellite",
        "tidyverse",
        "s2",
        "terra",
        "foreign",
        "raster",
        "sfnetworks",
        "spatstat",
        "mapproj",
        "OpenStreetMap",
        "gdalUtilities",
        "mapview",
        "tigris",
    )

    depends_on("r@4.6.1", when="@1.5-18_R4.6.1", type=("build", "run"))
    depends_on("r@4.5.3", when="@1.5-18_R4.5.3", type=("build", "run"))

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gdal")
    depends_on("proj")
    depends_on("geos")
    # depends_on("pkgconfig", type="build")
    depends_on("netcdf-fortran")
    depends_on("hdf5+hl+cxx+fortran")
    depends_on("java", type=("build", "run"))
