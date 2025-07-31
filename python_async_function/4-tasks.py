#!/usr/bin/env python3
"""
4-tasks.py

Define task_wait_n that schedules task_wait_random(max_delay) n times
and returns itself results in ascending completion order.
"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n asyncio.Tasks via task_wait_random(max_delay).

    Args:
        n (int): how many tasks to run concurrently.
        max_delay (int): maximum delay for each task.

    Returns:
        List[float]: list of delay values, ordered by completion time.
    """
    # 1. Kick off n tasks immediately:
    tasks: List[asyncio.Task[float]] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    # 2. As each Task finishes, await it and record its result:
    results: List[float] = []
    for finished in asyncio.as_completed(tasks):
        delay = await finished
        results.append(delay)

    return results


