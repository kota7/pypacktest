# -*- coding: utf-8 -*-

import numpy as np
from pkg_resources import resource_stream


def sumproduct(x, y):
    return np.dot(np.array(x), np.array(y))


def magic_square(n):
    if n in [3, 4]:
        x = np.load(resource_stream(__name__, 'magic_square/%d.npy' % n))
        return x
    else:
        print('"n" must be 3 or 4')
        