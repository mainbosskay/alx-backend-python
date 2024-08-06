#!/usr/bin/env python3
"""Module for async function async_generator is established"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yields 10 random float numbers between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
