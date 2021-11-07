#!/usr/bin/env python3
from os.path import dirname, join
import setuptools
import PYSlots.__init__ as __init__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PYSlots",
    version=__init__.VERSION,
    author="Lukas-Batema",
    author_email="lukasbatema@gmail.com",
    description="A little fun terminal Python Slots game!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lukas-Batema/pyslots",
    project_urls={
        "Bug Tracker": "https://github.com/Lukas-Batema/pyslots/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["pyslots"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pyslots=PYSlots.__main__:main",
        ]
    },
)
