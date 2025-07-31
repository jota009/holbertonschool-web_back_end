#!/usr/bin/env python3
"""
2-measure_runtime.py

Measure the average execution of wait_n(n, max_delay).
"""


import time
import asyncio
from typing import Any, Union, List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Spawn n coroutines via wait_n(max_delay), measure total elapsed time,
    and return the average time per coroutine.

    Args:
        n (int): Number of concurrent tasks.
        max_delay (int): Maximum delay passed to each wait_random call.

    Returns:
        float: Average runtime in seconds (total_time / n).
    """
    start_time = time.time()   # Start the timer
    asyncio.run(wait_n(n, max_delay))   # Execute all tasks
    total_time = time.time() - start_time   # Elapsed seconds
    return total_time / n   # Average per task
