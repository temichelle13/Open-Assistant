# setup.py for the shared python modules

from distutils.core import setup

from setuptools import find_namespace_packages

setup(
    name="oasst-shared",
    version="1.0",
    packages=find_namespace_packages(),
    author="OASST Team",
    install_requires=[
        "pydantic==1.10.13",
        "aiohttp==3.9.4",
        "aiohttp[speedups]",
    ],
)
