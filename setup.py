#!/usr/bin/env python
from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="uwufierpy",
    version="1.0.0",
    packages=["uwufier"],
    rust_extensions=[RustExtension("uwufier.uwupy")],
    extras_require={"dev": ["pytest", "flake8", "black"]},
    include_package_data=True,
    zip_safe=False,
)
