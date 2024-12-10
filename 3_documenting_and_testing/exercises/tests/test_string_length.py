#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Aung Myin Moe
"""

import unittest

from ..string_length import string_length

class TestStringLength(unittest.TestCase):
    """Test the string_length function"""
    
    def test_0(self):
        """It should evaluate 'superman' to 8"""
        actual = string_length('superman') # call function with test arguments
        expected = 8 # hand-write the expected return value
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate '' to None"""
        actual = string_length('')
        expected = None
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate '24567' to 5"""
        actual = string_length('24567')
        expected = 5
        self.assertEqual(actual, expected)
        
    def test_not_a_string(self):
        """It should raise an assertion error if the argument is not a string"""
        with self.assertRaises(AssertionError):
            string_length(5)
