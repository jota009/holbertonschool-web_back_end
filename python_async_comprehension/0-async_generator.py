#!/usr/bin/env python3
"""
0-async_generator.py

Asynchronous generator that yields 10
random floats between 0 and 10, wiat 1 second
before each yield.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield a random float between 0 and 10 every second, 10 times.

    Yields:
        float: A random number in [0, 10].
    """
    for _ in range(10):
        # 1. Pause this generator for 1 second without blocking the loop
        await asyncio.sleep(1)
        # 2. Produce a random float in [0, 10]
        yield random.uniform(0, 10)
