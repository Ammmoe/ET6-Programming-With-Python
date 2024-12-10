#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Aung Myin Moe
"""

import unittest

from ..bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    """Test the bubble_sort function"""
    
    def test_0(self):
        """It should evaluate [] to []"""
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate [0] to [0]"""
        actual = bubble_sort([0])
        expected = [0]
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate [8, 5, 4, 2, 9] to [2, 4, 5, 8, 9]"""
        actual = bubble_sort([8, 5, 4, 2, 9])
        expected = [2, 4, 5, 8, 9]
        self.assertEqual(actual, expected)
        
    def test_3(self):
        """It should evaluate [1, 2, 3, 4, 5] to [1, 2, 3, 4, 5]"""
        actual = bubble_sort([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)
        
    def test_not_a_list(self):
        """It should raise an assertion error if the argument is not a list of integers"""
        with self.assertRaises(AssertionError):
            bubble_sort(1)
            
    def test_not_an_int(self):
        """It should raise an assertion error if the argument is not a list of integers"""
        with self.assertRaises(AssertionError):
            bubble_sort([9.2, 8.22, 8])
