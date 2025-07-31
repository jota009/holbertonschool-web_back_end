#!/usr/bin/env python3
"""
9-element_length.py

Annotate element_length to accept any iterable of sequences
and return a list of (element, length) tuples.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given an iterable of sequence-like objects, return a list
    of tuples pairing each element with its length.

    Args:
        lst (Iterable[Sequence]): An iterable whose items support len().

    Returns:
        List[Tuple[Sequence, int]]: A list of (item, len(item)) tuples.
    """
    return [(i, len(i)) for i in lst]
