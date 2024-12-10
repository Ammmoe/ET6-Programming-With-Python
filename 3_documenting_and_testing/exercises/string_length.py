#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the length of a string

Module contents:
    - string_length: generates the length of a string input.

Created on XX XX XX
@author: Aung Myin Moe
"""


def string_length(text: str) -> int:
    """Generates the string length of an input text

    Args:
        text (str): must be a string

    Returns:
        int: the length of the text argument is returned as an integer
        
    Raises:
        AssertionError: if the argument is not a string
        
    >>> string_length('superman')
    8
    
    >>> string_length('')
    
    
    >>> string_length('24567')
    5
    """
    
    # User input must be a string
    assert isinstance(text, str), "Text is not a string."
    
    # Consider a return case if the user inputs an empty string
    if len(text) == 0:
        return None

    # If the text is not empty, return the string length
    return len(text)
