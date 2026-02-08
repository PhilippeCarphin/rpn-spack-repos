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
#     spack install librmn
#
# You can edit this file again by typing:
#
#     spack edit librmn
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

def submodules(package):
    return ["dep/json-c", "dep/udunits2", "App"]

class Librmn(CMakePackage):
    """A library of functions for numerical weather prediction used
    primarily by Environment and and Climate Change Canada.

    Its main components are Standard RPN files and the EZ interpolator."""

    homepage = "https://github.com/ECCC-ASTD-MRD/librmn"
    git = homepage
    url = "librmn"

    maintainers("rpn-si")

    license("LGPL-2.1-only", checked_by="pc")

    version("master", branch="master", submodules=submodules)
    version("dev_alpha", branch="dev_alpha", submodules=submodules)
    version("WIP-m2-build", branch="WIP-m2-build", submodules=submodules)

    variant("mpi", default=False)

    depends_on("cmake-rpn", type="build")

    with when("+mpi"):
        depends_on("openmpi")

    with when("platform=darwin") or when("target=aarch64"):
        requires("@WIP-m2-build", msg="Only WIP-m2-build can be built on darwin")
        requires("-mpi", msg="Not doing mpi stuff for now on darwin")

    # Haven't tested if this makes a difference
    provides("app")

    def cmake_args(self):
        args = []
        with when("-mpi"):
            args.append("-DWITH_OMPI=OFF")
        return args
