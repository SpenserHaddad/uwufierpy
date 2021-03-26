#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="uwufierpy",
    version="0.1.0",
    packages=["uwufier"],
    rust_extensions=[RustExtension("uwufier.uwupy")],
    include_package_data=True,
    zip_safe=False,
)