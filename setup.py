#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['docopt', 'sphinx', 'autodoc', 'coverage',
                'flake8', 'chardet']  # TODO: put package requirements here

setup(
    name='rt_hack',
    version='0.0.1',
    description="A bunch of tests to determine the vulnerability of an IoT device",
    url='https://github.com/Kthulhuk/RT_Hack',
    author="Jean-Hieu HUYNH",
    author_email='jean-hieu.huynh@ensea.fr',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rt_hack = rt_hack.__init__:main'
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU Affero General Public License v3",
    keywords='rt_hack',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
