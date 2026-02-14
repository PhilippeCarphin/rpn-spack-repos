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
#     spack install cmake-rpn
#
# You can edit this file again by typing:
#
#     spack edit cmake-rpn
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

import os


class CmakeRpn(CMakePackage):
    """CMake modules used by RPN-SI projects."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git = "https://github.com/ECCC-ASTD-MRD/cmake_rpn"

    maintainers("RPN-SI")
    license("LGPL-2.1-only", checked_by="pc")

    def setup_dependant_build_environment(self, env, dep_spec):
        env.set("EC_CMAKE_MODULE_PATH", f"{self.home}/modules")

    def setup_run_environment(self, env):
        env.set("EC_CMAKE_MODULE_PATH", f"{self.home}/modules")

    version("dev", branch="dev")
    version("WIP-m2-build", branch="WIP-m2-build")
    with when("platform=darwin"):
        requires("@WIP-m2-build")

    # I think it's the fact that MacOS is weirdly half case sensitive so vgrid's
    # find_package(rmn) gets the FindRMN.cmake file from this repo.  Just remove
    # it.  We could also add a patch to vgrid so it does
    # find_package(rmn REQUIRED CONFIG)
    # but since we would have to do that for every package that uses rmn this
    # way, I think this is more simple and anyway that find module should be
    # removed I think.
    @when("platform=darwin")
    def patch(self):
        os.remove("modules/FindRMN.cmake")
        os.remove("modules/FindVGRID.cmake")
