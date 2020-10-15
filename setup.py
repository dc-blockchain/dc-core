#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This file was generated with PyScaffold 3.0.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup
import versioneer

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
    start_dc = dc.main:main
    dc_start = dc.main:main
    dc = dc.cli:main
    dc_grpc_proxy = dc.grpcProxy:main
    dc_measure = dc.measure:main
    dc_walletd = dc.daemon.walletd:main
    dc_generate_genesis = dc.tools.generate_genesis:main
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points=entry_points,
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass(),
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
