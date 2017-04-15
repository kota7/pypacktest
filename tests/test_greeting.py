#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from testpack.greeting import give_quote, say_hello


class TestHello(unittest.TestCase):
    
    def test_hello(self):
        self.assertIsNone(say_hello())

class TestQuote(unittest.TestCase):
    
    def test_quote(self):
        self.assertIsNone(give_quote())

if __name__ == '__main__':
    unittest.main()
