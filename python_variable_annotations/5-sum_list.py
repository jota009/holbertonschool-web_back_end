#!/usr/bin/env python3
"""
5-sum_list.py

Define a function that sums a list of floats, with full type annotations.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all floats in input_list:

    Args:
        input_list (List[float]): A list wher every element is a float.

    Returns:
        float: The total sum of the list's elements.
    """
    return sum(input_list)
