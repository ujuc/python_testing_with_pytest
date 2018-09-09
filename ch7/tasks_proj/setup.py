#!/usr/bin/evn python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tasks',
    version='0.1.1',
    author='Thomas ujuc',
    author_email='sungjin.kang@ujuc.me',
    description='Pytest example Task App',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['tasks'],
    package_dir={'tasks': 'src/tasks'},
    install_requires=[
        'pytest', 'tinydb', 'pymongo',
    ],
)
