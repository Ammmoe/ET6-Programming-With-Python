#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string exists in at least one of the two given lists of strings.

Module contents:
    - is_in function
    
Created on 16-Dec-2024
@author: Aung Myin Moe
"""


# ---- define function ----
def is_in(list_1: list[str], list_2: list[str], string: str) -> bool:
  """Checks if a string exists in at least one of the two lists of strings.

  Args:
    list_1 (list[str]):  a list of strings to check
    list_2 (list[str]):  a list of strings to check
    string (str): the function will check if at least one of the lists have this string

  Returns:
    bool: return true if the item is in only one of the lists.
    
  Raises: AssertionError
    - if list_1 and list_2 are not lists
    - if the lists do not contain strings
    - if the argument string is not a string
    
  >>> is_in(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Bruno Mars'], 'Westlife')
  True
  
  >>> is_in(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Westlife'], 'Westlife')
  True
  
  >>> is_in(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Bruno Mars'], 'Aung Myin Moe')
  False
  
  >>> is_in([], [], '')
  True
  """
  assert isinstance(list_1, list), "The first input must be a list."
  assert isinstance(list_2, list), "The second input must be a list."
  assert isinstance(string, str), "The last input must be a string."
  assert all(isinstance(element, str) for element in list_1), "All elements in list_1 must be strings."
  assert all(isinstance(element, str) for element in list_2), "All elements in list_2 must be strings."
  
  # Loop through both lists to find the string
  if (list_1 == [] or list_2 == []) and string == '':
    return True
  elif string not in list_1 and string not in list_2:
    return False
  else:
    return True
