# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy", "greeting_ext"
    ],
    dependency_links=["git+https://github.com/kota7/pypacktest2.git"]
    package_data={
        'testpack': ['wilde.txt', 'magic_square/*.npy']
    },
    scripts=['bin/oscar-wilde'],
    entry_points={
        'console_scripts': ['magic-square=testpack.command:magic_square']
    }
)




