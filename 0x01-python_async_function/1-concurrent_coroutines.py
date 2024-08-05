#!/usr/bin/env python3
"""Module for async function wait_n is established"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times and returns list of result wait times"""
    delay_random = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_random)
