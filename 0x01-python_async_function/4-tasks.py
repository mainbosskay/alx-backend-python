#!/usr/bin/env python3
"""Module for async function task_wait_n is established"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns list of wait times"""
    delay_random = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_random)
