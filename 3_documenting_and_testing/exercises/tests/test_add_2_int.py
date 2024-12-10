#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Aung Myin Moe
"""

import unittest

# --- import function for documenting and testing ---

from ..add_2_int import add_2_int


class TestAdd2Int(unittest.TestCase):
    """Test the add_2_int function"""
    
    def test_0(self):
        """It should evaluate 0 for (0, 0)"""
        actual = add_2_int(0, 0) # call function with test arguments
        expected = 0 # hand-write the expected return value
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate 200 for (100, 100)"""
        actual = add_2_int(100, 100)
        expected = 200
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate 999999 for (444444, 555555)"""
        actual = add_2_int(444444, 555555)
        expected = 999999
        self.assertEqual(actual, expected)
        
    def test_not_an_int(self):
        """It should raise an assertion error if the argument is not an int"""
        with self.assertRaises(AssertionError):
            add_2_int(4.5, 1)
