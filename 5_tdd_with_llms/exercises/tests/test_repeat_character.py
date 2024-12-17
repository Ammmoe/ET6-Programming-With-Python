#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for repeat_character function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical strings, chars, and integers
    - Edge cases: space inputs, capital letters, and the times_to_repeat set to 0
    - Defensive tests: invalid inputs
    
Created on 17-Dec-2024

@author: Aung Myin Moe
"""

import unittest

from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Test suite for repeat_character function"""
    
    # Standard test cases
    def test_0(self):
        """A standard case for the basic functionality"""
        expected = 'supermaaan'
        actual = repeat_character('superman', 'a', 3)
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """A standard case with a capital letter"""
        expected = 'DDreadful'
        actual = repeat_character('Dreadful', 'D', 2)
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """A standard case for two letters to repeat"""
        expected = 'AungMMyinMMoe'
        actual = repeat_character('AungMyinMoe', 'M', 2)
        self.assertEqual(actual, expected)
        
    # Edge cases
    def test_3(self):
        """A case where the string does not contain the char_to_repeat"""
        expected = 'danger'
        actual = repeat_character('danger', 'x', 4)
        self.assertEqual(actual, expected)
        
    def test_4(self):
        """A case where small d is used as the char_to_repeat for the capital D in the string"""
        expected = 'Donkey'
        actual = repeat_character('Donkey', 'd', 4)
        self.assertEqual(actual, expected)
        
    def test_5(self):
        """A case where a space is repeated in the string"""
        expected = 'space   man'
        actual = repeat_character('space man', ' ', 3)
        self.assertEqual(actual, expected)
        
    def test_6(self):
        """A case where the argument times_to_repeat is set to 0"""
        expected = 'sndr'
        actual = repeat_character('sandar', 'a', 0)
        self.assertEqual(actual, expected)
        
    # Defensive cases
    def test_7(self):
        """A case where the argument string is not a string"""
        with self.assertRaises(AssertionError):
            repeat_character(4, 'a', 3)
            
    def test_8(self):
        """A case where the argument char_to_repeat is an empty string"""
        with self.assertRaises(AssertionError):
            repeat_character('superman', '', 3)
            
    def test_9(self):
        """A case where the argument char_to_repeat is more than one char in length"""
        with self.assertRaises(AssertionError):
            repeat_character('superman', 'an', 4)
            
    def test_10(self):
        """A case where the argument char_to_repeat is not a string"""
        with self.assertRaises(AssertionError):
            repeat_character('superman', 3, 3)
            
    def test_11(self):
        """A case where the argument times_to_repeat is not an int"""
        with self.assertRaises(AssertionError):
            repeat_character('superman', 's', 5.5)
            
    def test_12(self):
        """A case where the argument times_to_repeat is a negative integer"""
        with self.assertRaises(AssertionError):
            repeat_character('superman', 's', -1)
            