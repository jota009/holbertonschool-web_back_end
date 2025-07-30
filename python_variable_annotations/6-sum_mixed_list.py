#!/usr/bin/env python3
"""
6-sum_mixed_list.py

Define a function that sums a list of ints and floats,
with full type annotations.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of all numbers in mxd_lst.

    Args:
        mxd_lst (List[Union[int, float]]):
            A list where each element is either an int or a float.

    Returns:
        float: The total sum of all elements.
    """
    return float(sum(mxd_lst))
