#!/usr/bin/env python3
"""
2-measure_runtime.py

Measure the runtime of four parallel async comprehensions.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension() four times in parallel, measure elapsed time,
    and return it.

    Returns:
        float: Total time in seconds to complete all four runs.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
