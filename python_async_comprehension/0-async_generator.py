#!/usr/bin/env python3
"""
0-async_generator.py

Asynchronous generator that yields 10 random floats between 0 and 10,
waiting 1 second before each yield.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield a random float between 0 and 10 every second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
