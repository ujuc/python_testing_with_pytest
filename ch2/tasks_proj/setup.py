#!/usr/bin/evn python

from distutils.core import setup
import pkg_resources

setup(
    name='tasks',
    version=pkg_resources.require('tasks')[0].version,
    packages=['tasks'],
    package_dir={'tasks': 'src/tasks'},
)
