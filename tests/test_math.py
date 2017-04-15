#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import numpy as np

from testpack.math import magic_square, sumproduct

class TestMagic(unittest.TestCase):

    def magic_helper(self, n):
        x = magic_square(n)
        if not (n in [3, 4]):
            # x should be None, no further test
            self.assertIsNone(x)
            return
        
        # first, x must be 2-dim numpy array
        self.assertIsInstance(x, np.ndarray)
        self.assertEqual(len(x.shape), 2)
        # and each size must be n 
        self.assertEqual(x.shape[0], n)
        self.assertEqual(x.shape[1], n)

        # as a magic square, row-sums, col-sums, diag-sums 
        # must be all equal
        all_sums = np.concatenate([
            x.sum(axis=1), # row sums
            x.sum(axis=0)  # col sums
        ])
        # diag sums
        all_sums = np.append(all_sums, x.trace()) 
        all_sums = np.append(all_sums, np.fliplr(x).trace()) 
        self.assertEqual(np.unique(all_sums).size, 1) 
    
    def test_magic3(self):
        self.magic_helper(3)

    def test_magic4(self):
        self.magic_helper(4)

    def test_magic5(self):
        self.magic_helper(5)
    
    def test_magic_others(self):
        for n in range(0,3):
            self.magic_helper(n)
        for n in range(6,11):
            self.magic_helper(n)


if __name__ == '__main__':
    unittest.main()

