#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string exists in only one of the two given lists of strings.

Module contents:
    - is_in_one function
    
Created on 15-Dec-2024
@author: Aung Myin Moe
"""

# ---- define function ----
def is_in_one(list_1: list[str], list_2: list[str], string: str) -> bool:
  """Checks if a string exists in only one of the two lists of strings.

  Args:
    list_1 (list[str]):  a list of strings to check
    list_2 (list[str]):  a list of strings to check
    string (str): the function will check if only one of the lists have this string

  Returns:
    bool: return true if the item is in only one of the lists.
    
  Raises: AssertionError
    - if list_1 and list_2 are not lists
    - if the lists do not contain strings
    - if the argument string is not a string
    
  >>> is_in_one(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Bruno Mars'], 'Westlife')
  True
  
  >>> is_in_one(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Westlife'], 'Westlife')
  False
  
  >>> is_in_one(['Westlife', 'Akon', 'Queen'], ['Avril Lavigne', 'Lady Gaga', 'Bruno Mars'], 'Aung Myin Moe')
  False
  
  >>> is_in_one([], [], '')
  False
  """
  assert isinstance(list_1, list), "The first input must be a list."
  assert isinstance(list_2, list), "The second input must be a list."
  assert isinstance(string, str), "The last input must be a string."
  assert all(isinstance(element, str) for element in list_1), "All elements in list_1 must be strings."
  assert all(isinstance(element, str) for element in list_2), "All elements in list_2 must be strings."
  
  # Loop through both lists to find the string
  if string not in list_1:
    if string in list_2:
      return True
    return False
  elif string in list_1:
    if string in list_2:
      return False
    return True
