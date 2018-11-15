#!/usr/build/env python
# -*- coding: utf-8 -*-

from os import getcwd, path

from setuptools import setup, find_packages

with open(path.join(getcwd(), 'README.md'), mode='r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ontology-ddxf-crypto',
    version='0.0.2',
    description="""Ontology DDXF Cryptography Components""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='NashMiao',
    author_email='wdx7266@outlook.com',
    url='https://github.com/NashMiao/ontology-ddxf-crypto',
    maintainer='NashMiao',
    maintainer_email='wdx7266@outlook.com',
    # include_package_data=True,
    py_modules=['punica'],
    python_requires='>=3.5,<4',
    install_requires=[
        'ecdsa',
        'pycryptodomex',
        'ontology-python-sdk',
    ],
    license="GNU Lesser General Public License v3 (LGPLv3)",
    zip_safe=False,
    entry_points={
        'console_scripts': ["punica=punica.cli:main"],
    },
    packages=find_packages(exclude=["test*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
