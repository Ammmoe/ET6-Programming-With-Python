#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting a list of numbers in the ascending order

Module contents:
    - bubble_sort: sort a list of numbers using the bubble sort algorithm

Created on XX XX XX
@author: Aung Myin Moe
"""


def bubble_sort(original_list: list[int]) -> list[int]:
    """Sort a list of numbers in the ascending order using bubble sort algorithm

    Args:
        original_list: list[int]

    Returns:
        list[int]: returns the sorted list in the ascending order
        
    Raises:
        AssertionError: if the argument is not a list of integers
        
    >>> bubble_sort([])
    []
    
    >>> bubble_sort([0])
    [0]
    
    >>> bubble_sort([8, 5, 4, 2, 9])
    [2, 4, 5, 8, 9]
    
    >>> bubble_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """
    
    # the input must be a list of integers
    assert isinstance(original_list, list), "Input is not a list of integers"
    assert all(isinstance(i, int) for i in original_list), "Input is not a list of integers"

    # Iterate through the list and compare the int at position j with the int at position j+1
    # If int at j > int at j+1 -> swap two positions. Else, do nothing.    
    length = len(original_list)
    
    for i in range(length):
        for j in range(0, length - i - 1):
            if original_list[j] > original_list[j + 1]:
                original_list[j], original_list[j + 1] = original_list[j + 1], original_list[j]
                
    return original_list
