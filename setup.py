# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    test_requires=[
        'pytests'
    ],
    package_data={
        'testpack': ['wilde.txt', 'magic_square/*.npy']
    },
    scripts=['bin/oscar-wilde'],
    entry_points={
        'console_scripts': ['magic-square=testpack.command:magic_square']
    },
    test_suite='tests'
)




