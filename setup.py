#!/usr/bin/env python3

from setuptools import setup, find_packages

def readme():
    with open('README.md') as file:
        return file.read()

setup(name='radioid_utils',
      version='0.1.0',
      description='Utilities for working with radioid.net databases',
      long_description='Modules for maintaining a local cache of radioid.net databases with automatic updating, and easy access from other code',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3.7',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Communications :: Ham Radio',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ],
      keywords='dmr digital radioid dmrid ccs7 ham amateur radio',
      author='Jim Gifford, K9AGR',
      author_email='k9agr@giffords.net',
      install_requires=[],
      license='GPLv3',
      url='https://github.com/k9agr/radioid_utils',
      packages=find_packages()
     )
