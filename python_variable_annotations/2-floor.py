#!/usr/bin/env python3
"""
2-floor.py: Define a function that returns the floor of a float,
with full type annotations.
"""


import math


def floor(n: float) -> int:
    """
    Return the floor of n.

    Args:
        n (float): The number to floor.

    Returns:
        int: The greatest integer <= n.
    """
    return math.floor(n)
