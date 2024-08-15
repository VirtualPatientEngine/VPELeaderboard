#!/usr/bin/env python3

'''Setup script for the package.'''

# import os
from setuptools import setup

# Get version from environment variable defined during the GitHub Action
# print ('new vesion', version)

setup(
    # Name of the package
    name='demoMLsourceCode',
    # read the version from the file release-version.txt (do not change this line)
    version=open('release_version.txt', encoding='utf-8').read().strip(),
    # Folders where the packages are located
    packages=['app', 'app/model', 'app/data'],
    # Author information
    author='Singh, Gurdeep',
    author_email='gsingh@bio.mx',
    # Description of the package
    description='Demo template to write source code to build ML models',
    # URL for the team or package
    url='https://bio.mx/research-teams/artificial-intelligence/team-vpe/',
    license='MIT',
)
