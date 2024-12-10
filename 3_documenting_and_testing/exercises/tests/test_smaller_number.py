#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Aung Myin Moe
"""

import unittest

from ..smaller_number import smaller_number


class TestSmallerNumber(unittest.TestCase):
    """Test the smaller_number function"""
    
    def test_0(self):
        """It should evaluate (6, 5) to 5"""
        actual = smaller_number(6, 5)
        expected = 5
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate (877, 882) to 877"""
        actual = smaller_number(877, 882)
        expected = 877
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate (1, 1) to 2"""
        actual = smaller_number(1, 1)
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            smaller_number(9.5, 8.2)
