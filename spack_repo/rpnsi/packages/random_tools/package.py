from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RandomTools(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ECCC-ASTD-MRD/random_tools"
    git = homepage

    maintainers("rpn-si")

    license("LGPL-2.1-only", checked_by="pc")

    version("master", branch="master")
    version("dev", branch="dev")
    version("WIP-m2-build", branch="WIP-m2-build")

    depends_on("cmake-rpn", type="build")
    requires("@WIP-m2-build", when="platform=darwin")
    # depends_on("librmn", type="build")
    # depends_on("tdpack", type="build", when="+tdpack")

    # patch("no_rmn_req_version.patch")
    # patch("sketchy_arg_mismatch_fix.patch")
    # patch("remove_link_options.patch")
