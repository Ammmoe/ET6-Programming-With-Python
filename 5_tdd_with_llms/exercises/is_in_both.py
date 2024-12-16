#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string exists in given two lists of strings.

Module contents:
    - is_in_both function
    
Created on 15-Dec-2024
@author: Aung Myin Moe
"""


# ---- define function ----
def is_in_both(list_1: list[str], list_2: list[str], string: str) -> bool:
  """Checks if a string exists in given two lists of strings.

  Args:
    list_1 (list[str]): a list of strings to check
    list_2 (list[str]): a list of strings to check
    string (str): the function will check if both of the lists have this string

  Returns:
    bool: return true if the item is in both of the lists.
      
  Raises: AssertionError
    - if list_1 and list_2 are not lists
    - if the lists do not contain strings
    - if the argument string is not a string
    
  >>> is_in_both(['apple', 'orange', 'strawberry', 'blackberry'], ['strawberry', 'cucumber', 'delusional'], 'strawberry')
  True
  
  >>> is_in_both(['steel', 'iron', 'carbon'], ['airplane', 'aluminum', 'manganese'], 'katana')
  False
  
  >>> is_in_both([], [], '')
  True
  """
  assert isinstance(list_1, list), "The first input must be a list."
  assert isinstance(list_2, list), "The second input must be a list."
  assert isinstance(string, str), "The last input must be a string."
  assert all(isinstance(element, str) for element in list_1), "All elements in list_1 must be strings."
  assert all(isinstance(element, str) for element in list_2), "All elements in list_2 must be strings."
  
  # Loop through both lists to find the string
  if list_1 == [] and list_2 == [] and string == '':
    return True
  elif string in list_1:
    if string in list_2:
      return True
  return False
  