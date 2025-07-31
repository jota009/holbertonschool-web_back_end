#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

Spawn wait_random n times concurrently and return their delays
in ascending order by processing tasks as they complete.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random(max_delay) n times concurrently.

    Args:
        n (int): number of concurrent coroutines to run.
        max_delay (int): maximum delay for each wait_random call.

    Returns:
        List[float]: list of delays, in ascending order, as each
                     coroutine completes.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results: List[float] = []
    for completed_future in asyncio.as_completed(tasks):
        delay = await completed_future
        results.append(delay)

    # 3. Return the naturally ordered list
    return results
