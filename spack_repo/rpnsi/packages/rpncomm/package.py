from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Rpncomm(CMakePackage):
    homepage = "https://github.com/ECCC-ASTD-MRD/rpncomm"
    git = homepage
    url = homepage

    maintainers("rpn-si")

    license("LGPL-2.1-only", checked_by="pc")

    version("main", branch="main")
    version("WIP-m2-build", branch="WIP-m2-build")
    requires("@WIP-m2-build", when="platform=darwin")
    depends_on("mpi")

    # One of those scripts or custom commands that generate files or change
    # stuff during the CMake process use sed and when it's BSD sed, it does
    # weird stuff.
    depends_on("sed", type="build")
    depends_on("cmake-rpn", type="build")
