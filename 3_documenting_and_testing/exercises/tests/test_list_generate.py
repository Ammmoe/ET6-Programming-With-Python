#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX
@author: Aung Myin Moe
"""

import unittest

from ..list_generate import list_generate


class TestListGenerate(unittest.TestCase):
    """Test the list_generate function"""
    
    def test_0(self):
        """It should evaluate 0 to []"""
        actual = list_generate(0)
        expected = []
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate 1 to [0]"""
        actual = list_generate(1)
        expected = [0]
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate 5 to [0, 1, 2, 3, 4]"""
        actual = list_generate(5)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)
        
    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            list_generate('super')
            
    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than zero"""
        with self.assertRaises(AssertionError):
            list_generate(-1)
