#!/usr/bin/env python3
"""
0-basic_async_syntax.py

Defines an async coroutine wait_random the waits for the random delay
between 0 and max_delay seconds and returns that delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum number of seconds
        to wait (inclusive). Defaults to 10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
