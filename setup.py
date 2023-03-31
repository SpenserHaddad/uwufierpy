#!/usr/bin/env python
from setuptools import setup
from setuptools_rust import RustExtension

setup(
    rust_extensions=[RustExtension("uwufier.uwupy")],
)
