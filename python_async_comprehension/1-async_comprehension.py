#!/usr/bin/env python3
"""
1-async_comprehension.py

Collect 10 random floats from async_generator
using an async comprehension.
"""


from typing import List


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Run async_generator and collect its 10 yielded values into a list
    using an async list comprehension.

    Returns:
        List[float]: The 10 random numbers yielded
        by async_generator.
    """
    return [value async for value in async_generator()]
