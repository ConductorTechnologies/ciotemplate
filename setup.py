#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import re
import setuptools

NAME = "ciocore"
DESCRIPTION = "Core functionality for Conductor's client tools"
URL = "https://github.com/AtomicConductor/conductor-core"
EMAIL = "info@conductortech.com"
AUTHOR = "conductor"
REQUIRES_PYTHON = "~=2.7"
REQUIRED = ["pyjwt>=1.4.2", "pyyaml>=3.11", "requests>=2.10.0"]
HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "src", NAME, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
    ],
    description=DESCRIPTION,
    entry_points={"console_scripts": ["conductor=conductor.cli.conductor:main"]},
    include_package_data=True,
    install_requires=REQUIRED,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    name=NAME,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude=["*.pyc"]),
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=VERSION,
    zip_safe=False,
)

