#!/usr/bin/env python3
"""
7-to_kv.py

Define `to_kv.py`
- k: a string key
- v: an integer or float
Returns a tuple (k,  v²), annotated as (str, float).
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Build a key-value tuple where the value is squared.

    Args:
        k (str): The key/name.
        v (Union[in, float]): The numeric value to the square.

    Returns:
        Tuple[str, float]: A tuple (k, v squared).
    """
    return (k, v * v)
