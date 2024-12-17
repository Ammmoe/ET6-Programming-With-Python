#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for modifying and returning a string with a given character repeated n times.

Module contents:
    - repeat_character function
    
Created on 17-Dec-2024
@author: Aung Myin Moe
"""


def repeat_character(string: str, char_to_repeat: str, times_to_repeat: int) -> str:
    """Modify a string with a given character repeated n times.

    Parameters:
        string (str): the string to modify
        char_to_repeat (str): the char in the string to repeat
        times_to_repeat (int): how many times the char will repeat in the modified string

    Returns:
        str: a string with the argument char repeated n times
        
    Raises: AssertionError
        - if the argument string is not a string
        - if the argument char_to_repeat is not a string with a length of 1
        - if the argument times_to_repeat is a negative integer
        
    >>> repeat_character('superman', 'a', 3)
    'supermaaan'
    
    >>> repeat_character('AungMyinMoe', 'M', 2)
    'AungMMyinMMoe'
    
    >>> repeat_character('danger', 'x', 4)
    'danger'
    
    >>> repeat_character('Donkey', 'd', 5)
    'Donkey'
    
    >>> repeat_character('space man', ' ', 3)
    'space   man'
    
    >>> repeat_character('sandar', 'a', 0)
    'sndr'
    """
    assert isinstance(string, str)
    assert isinstance(char_to_repeat, str) and len(char_to_repeat) == 1
    assert isinstance(times_to_repeat, int) and times_to_repeat >= 0
    
    # Function implementation here
    result = ''
    
    if char_to_repeat not in string:
        return string
    else:
        for char in string:
            if char != char_to_repeat:
                result = result + char        
            elif char == char_to_repeat:
                result = result + char * times_to_repeat
        return result
        