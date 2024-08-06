#!/usr/bin/env python3
"""Module for async function measure_runtime is established"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynchronously runs async_comprehension coroutine 4
    times in parallel and measures total execution time"""
    time_begin = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - time_begin
    return total_time
