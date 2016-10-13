#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='aprsfi',
    version='0.2',
    license='LGPLv3',
    description='python client aprs.fi API.',
    long_description='A complete Python client for aprs.fi',
    packages=['aprsfi'],
    author="Whanderley Souza Freitas",
    author_email='whanderley.souza@iff.edu.br',
    install_requires=['requests'],
    url='https://github.com/SAEG-DSE/aprsfi',
    download_url='https://github.com/SAEG-DSE/python-aprsfi/archive/0.2.tar.gz',
    keywords='aprsfi api client wrapper',
)
