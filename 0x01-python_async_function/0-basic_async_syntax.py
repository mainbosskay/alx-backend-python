#!/usr/bin/env python3
"""Module for async function wait_random is established"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random duration of up to max_delay"""
    delay_random = random.random() * max_delay
    await asyncio.sleep(delay_random)
    return delay_random
