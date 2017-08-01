#!/usr/bin/env python
from setuptools import setup
import os
import sys

__doc__ = """
Command line tool and library wrappers around iwlist and
/etc/network/interfaces.
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'setuptools',
    'pbkdf2',
]
try:
    import argparse
except ImportError:
    install_requires.append('argparse')

version = '1.0.0'

should_install_cli = os.environ.get('WIFI_INSTALL_CLI') not in ['False', '0']
command_name = os.environ.get('WIFI_CLI_NAME', 'pyiw')

entry_points = {}
data_files = []

if should_install_cli:
    entry_points['console_scripts'] = [
        '{command} = pyiw.cli:main'.format(command=command_name),
    ]
    # make sure we actually have write access to the target folder and if not don't
    # include it in data_files
    if os.access('/etc/bash_completion.d/', os.W_OK):
        data_files.append(('/etc/bash_completion.d/', ['extras/wifi-completion.bash']))
    else:
        print("Not installing bash completion because of lack of permissions.")

setup(
    name='pyiw',
    version=version,
    author='Leonardo Lazzaro',  # Original authors: Rocky Meza, Gavin Wahl project was deprecated.
    author_email='lazzaroleonardo@gmail.com',
    description=__doc__,
    long_description='Wifi is command that makes it easier to connect the WiFi networks from the command line.',
    packages=['pyiw'],
    entry_points=entry_points,
    test_suite='tests',
    platforms=["Debian"],
    license='BSD',
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Networking",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
    data_files=data_files
)
