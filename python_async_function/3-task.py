#!/usr/bin/env python3
"""
3-tasks.py

Define a synchronous function task_wait_random that schedules
wait_random(max_delay) as an asyncio.Task and returns it.
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Schedule wait_random(max_delay) as a Task and return it.

    Args:
        max_delay (int): Maximum delay to pass along.

    Returns:
        asyncio.Task: A Task object that will run the coroutine.
    """
    # create_task immediately schedules the coroutine on the running loop
    return asyncio.create_task(wait_random(max_delay))
