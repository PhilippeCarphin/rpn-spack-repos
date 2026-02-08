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
#     spack install tdpack
#
# You can edit this file again by typing:
#
#     spack edit tdpack
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Tdpack(CMakePackage):
    """It's Tdpack, what can I say"""

    homepage = "https://github.com/ECCC-ASTD-MRD/tdpack"
    git = homepage

    maintainers("rpn-si")

    license("LGPL-2.1-only", checked_by="pc")

    version("master", branch="master")

    variant("mpi", default=False)

    depends_on("cmake-rpn", type="build")
    depends_on("librmn", type="build")

    with when("+mpi"):
        depends_on("openmpi")

    def cmake_args(self):
        args = []
        with when("-mpi"):
            args.append("-DWITH_OMPI=OFF")
        return args
