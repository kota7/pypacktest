# -*- coding: utf-8 -*-
"""
Math Related Test Functions
"""


import numpy as np
from pkg_resources import resource_stream


def sumproduct(x, y):
    """
    Compute the sum of elementwise product of two vectors
    
    :param x: vector
    :param y: vector
    :type x: list of numbers or 1-dim numpy.array
    :type y: list of numbers of 1-dim numpy.array
    :return: sum of elementwise product of x and y
    :rtype: number
    """
    return np.dot(np.array(x), np.array(y))


def magic_square(n):
    """
    Return a magic square of specified size
    
    :param n: size of magic square
    :type n: int
    :return: magic square of size n if n is supported. Otherwise None
    :rtype: 2-dim numpy.array of shape (n,n) if supported. Otherwise None
    """
    if n in [3, 4]:
        with resource_stream(__name__, 'magic_square/%d.npy' % n) as f:
            x = np.load(f)
        return x
    else:
        print('"n" must be 3 or 4')
        