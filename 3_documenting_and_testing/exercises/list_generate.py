#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating a list of numbers

Module contents:
    - list_generate: generates a list of first n numbers

Created on XX XX XX
@author: Aung Myin Moe
"""

def list_generate(length: int) -> list[int]:
    """Generates a list of first n numbers according to the user input integer (n)
    
    Args:
        length (int): greater than or equal to zero

    Returns:
        list[int]: a list of first n numbers
        
    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if the argument is less than zero
        
    >>> list_generate(0)
    []
    
    >>> list_generate(1)
    [0]
    
    >>> list_generate(5)
    [0, 1, 2, 3, 4]
    """
    
    # The argument must be an integer not less than zero
    assert isinstance(length, int), "user input is not an integer"
    assert length >= 0, "user input is less than 0"

    # Generates a list of numbers based on the user input integer    
    list_output = []

    number = 0
    while len(list_output) < length:
        list_output.append(number)
        number = number + 1

    return list_output
