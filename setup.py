#!/usr/bin/env python

from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="aws-shd-rss",
    description="Check AWS Service Health Dashboard RSS",
    version="0.1",
    author="htnosm",
    author_email="htnosm@gmail.com",
    license="MIT License",
    install_requires=_requires_from_file('requirements.txt'),
    python_requires=">=3.8",
)
