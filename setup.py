#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="aws-shd-rss",
    description="Check AWS Service Health Dashboard RSS",
    version="0.1",
    author="htnosm",
    author_email="htnosm@gmail.com",
    license="MIT License",
    url="https://github.com/htnosm/aws-shd-rss",
    packages=find_packages(),
    # Support Python 3.8 or greater
    python_requires=">=3.8",
)
