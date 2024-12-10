#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for evaluating a smaller number among the two arguments

Module contents:
    - smaller_number: generates a smaller number among two inputs

Created on XX XX XX
@author: Aung Myin Moe
"""


def smaller_number(number_1: int, number_2: int) -> int:
    """Evaluates a smaller number among the two arguments

    Args:
        number_1 (int): must be an int
        number_2 (int): must be an int

    Returns:
        float: the smaller number among the two arguments -> else, returns the sum of two numbers
        
    Raises:
        AssertionError: if the argument is not an int or float
        
    >>> smaller_number(6, 5)
    5
    
    >>> smaller_number(877, 882)
    877
    
    >>> smaller_number(1, 1)
    2
    """
    
    # The arguments should only be a float or an int
    assert isinstance(number_1, int), "First input is not an integer"
    assert isinstance(number_2, int), "Second input is not an integer"
    
    # Compare two numbers and choose the smaller one
    # Else, return the sum
    if number_1 < number_2:
        return number_1
    
    elif number_1 > number_2:
        return number_2
    
    else: 
        return number_1 + number_2
