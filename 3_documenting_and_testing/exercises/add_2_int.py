#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for adding two integers

Module contents:
    - add_2_numbers: it adds two integers.

Created on XX XX XX
@author: Aung Myin Moe
"""


def add_2_int(int_1: int, int_2: int) -> int:
    """Add two integers that the user inputs

    Args:
        int_1 (int): must be an integer
        int_2 (int): must be an integer

    Returns:
        int: returns the value after adding int_1 and int_2
        
    Raises:
        AssertionError: if the argument is not an integer
        
    >>> add_2_int(1, 1)
    2
    
    >>> add_2_int(29, 29)
    58
    
    >>> add_2_int(125, 125)
    250
    """
    
    # User input should be an integer
    assert isinstance(int_1, int), "User_input_1 is not an integer"
    assert isinstance(int_2, int), "User_input_2 is not an integer"
    
    # Sum two ints and return the result
    return int_1 + int_2
