#!/usr/bin/env python

import os
import sys
import codecs

from setuptools import Command, setup, find_packages
from commands import setup_timeseries, build_messages

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info")

REQUIRED_PACKAGES  = [
    'six>=1.8.0',
    'basho_erlastic>=2.1.1',
    'python3_protobuf>=2.4.1,<2.6.0'
]

def get_version_number():
    """
    Gets the version number from the arguments. If passed, the version argument must be removed from
    sys.argv so as not to cause problems with setuptools which can't deal with additional arguments
    being passed that it doesn't recognise.
    """
    for index, argument in enumerate(sys.argv):
        if argument == "--version":
            new_version = sys.argv[index + 1]
            del sys.argv[index: index + 2]
            return new_version
    return None

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme_md = f.read()
    long_description = readme_md

setup(
    name='nhs-riak',
    version=get_version_number(),
    description='NHS fork of the Python client for Riak',
    long_description=long_description,
    url="https://github.com/NHSDigital/nhs-riak-python-client",
    author="NHS Digital Spine Core DevOps Team",
    author_email="devops.core@nhs.net",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database'
    ],
    packages=find_packages(),
    package_data={'riak': ['erl_src/*']},
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    zip_safe=True,
    platforms='Platform Independent',
    test_suite='riak.tests.suite',
    project_urls={
        'Source': 'https://github.com/NHSDigital/spine-riak-python-client/',
    },
    cmdclass={
        'build_messages': build_messages,
        'setup_timeseries': setup_timeseries,
        "clean": CleanCommand
    }
)
