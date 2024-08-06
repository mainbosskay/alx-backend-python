#!/usr/bin/env python3
"""Module for async function async_comprehension is established"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously collects 10 random floats from an
    async generator and returns them as list"""
    return [num_random async for num_random in async_generator()]
