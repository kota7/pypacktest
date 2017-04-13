# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),
    
    install_requires=[ 
        "numpy"
    ],
    package_data={
        'testpack': ['wilde.txt', 'magic_square/*.npy']
    }
)




