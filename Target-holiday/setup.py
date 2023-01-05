#!/usr/bin/env python
from setuptools import setup

setup(
    name="Target-holiday",
    version="0.1.0",
    description="Singer.io target for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["Target_holiday"],
    install_requires=[
        "singer-python>=5.0.12",
    ],
    entry_points="""
    [console_scripts]
    Target-holiday=Target_holiday:main
    """,
    packages=["Target_holiday"],
    package_data = {},
    include_package_data=True,
)
