#!/usr/bin/env python3
"""
1-concat.py: Defina a function that concatenates two strings,
using full type annotations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Return the concatenation of str1 and str2.

    Args:
        str1 (str): The firts part of the result string.
        str2 (str): The second part to append.

    Returns:
        str: The combined text: str1 followed by str2.
    """
    return str1 + str2
