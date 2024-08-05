#!/usr/bin/env python3
"""Module for measure_time function is established"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Calculates average runtime of wait_n over number of executions"""
    time_begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - time_begin
    return total_time / n
