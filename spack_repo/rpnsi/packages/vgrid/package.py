# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install vgrid
#
# You can edit this file again by typing:
#
#     spack edit vgrid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Vgrid(CMakePackage):
    """It's vgrid, what can I say"""

    homepage = "https://github.com/ECCC-ASTD-MRD/vgrid"
    git = homepage

    maintainers("rpn-si")

    license("LGPL-2.1-only", checked_by="pc")

    variant("tdpack", default=True)

    version("master", branch="master")
    version("dev", branch="dev")

    depends_on("cmake-rpn", type="build")
    depends_on("librmn", type="build")
    depends_on("tdpack", type="build", when="+tdpack")

    patch("no_rmn_req_version.patch")
