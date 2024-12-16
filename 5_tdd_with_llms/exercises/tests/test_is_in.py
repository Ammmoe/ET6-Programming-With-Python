#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
  - Standard cases: typical string lists
  - Edge cases: empty lists and an empty string
  - Defensive tests: invalid inputs
    
Created on 16-Dec-2024

@author: Aung Myin Moe
"""

import unittest

from ..is_in import is_in


class TestIsIn(unittest.TestCase):
  """Test suite for the is_in function."""
  
  # Standard test cases
  def test_0(self):
    """A standard true case"""
    list_1 = ['Westlife', 'Akon', 'Queen']
    list_2 = ['Avril Lavigne', 'Lady Gaga', 'Bruno Mars']
    string = 'Westlife'
    self.assertEqual(is_in(list_1, list_2, string), True)
    
  def test_1(self):
    """A true case where the string is in both of the lists"""
    list_1 = ['Westlife', 'Akon', 'Queen']
    list_2 = ['Avril Lavigne', 'Lady Gaga', 'Westlife']
    string = 'Westlife'
    self.assertEqual(is_in(list_1, list_2, string), True)
    
  def test_2(self):
    """A false case where the string is in none of the lists"""
    list_1 = ['Westlife', 'Akon', 'Queen']
    list_2 = ['Avril Lavigne', 'Lady Gaga', 'Westlife']
    string = 'Aung Myin Moe'
    self.assertEqual(is_in(list_1, list_2, string), False)
    
  # Edge cases
  def test_3(self):
    """2 empty lists and an empty string"""
    list_1 = []
    list_2 = []
    string = ''
    self.assertEqual(is_in(list_1, list_2, string), True)
    
  def test_4(self):
    """2 empty lists and a string"""
    list_1 = []
    list_2 = []
    string = 'aung myin moe'
    self.assertEqual(is_in(list_1, list_2, string), False)
    
  def test_5(self):
    """1 empty list but the other list contains the string"""
    list_1 = ['jinja', 'flask', 'html', 'css']
    list_2 = []
    string = 'flask'
    self.assertEqual(is_in(list_1, list_2, string), True)
    
  def test_6(self):
    """an empty string"""
    list_1 = ['superman', 'spiderman', 'ironman']
    list_2 = ['wonderwoman', 'Thanos', 'antman']
    string = ''
    self.assertEqual(is_in(list_1, list_2, string), False)
    
  # Defensive cases
  def test_7(self):
    """list_1 have non-string elements"""
    list_1 = ['one-piece', 3, True, 'Myanmar']
    list_2 = ['Thailand', 'Myanmar', 'Singapore']
    string = 'Myanmar'
    with self.assertRaises(AssertionError):
      is_in(list_1, list_2, string)
      
  def test_8(self):
    """list_2 have non-string elements"""
    list_1 = ['Thailand', 'Myanmar', 'Singapore']
    list_2 = ['one-piece', 3, True, 'Myanmar']
    string = 'Myanmar'
    with self.assertRaises(AssertionError):
      is_in(list_1, list_2, string)
      
  def test_9(self):
    """argument string has non-string element"""
    list_1 = ['UK', 'US', 'Austria']
    list_2 = ['New Zealand', 'Singapore', 'Switzerland']
    string = 2
    with self.assertRaises(AssertionError):
      is_in(list_1, list_2, string)
