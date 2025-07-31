#!/usr/bin/env python3
"""
Define `make_multiplier`:
- Input: multiplier (float)
- Returns: a function f(x: float) -> float that computes x * multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its input by `multiplier`.

    Args:
        multiplier (float): The factor to apply.

    Returns:
        Callable[[float], float]: A function that takes a float x and returns x * multiplier.
    """
    def multiplier_fn(x: float) -> float:
        return x * multiplier

    return multiplier_fn
