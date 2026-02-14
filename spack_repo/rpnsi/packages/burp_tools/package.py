# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class BurpTools(CMakePackage):
    """Collection of tools to manipulate RPN standard files """
    homepage = "https://github.com/ECCC-ASTD-MRD/burp-tools"
    git = homepage
    url = "burp-tools"
    version("dev", branch="dev")
    version("master", branch="master")
    version("WIP-m2-build", branch="WIP-m2-build")

    requires("@WIP-m2-build", when="platform=darwin")

    patch("no_rmn_req_version.patch")

    depends_on("librmn")
    depends_on("cmake-rpn", type="build")
