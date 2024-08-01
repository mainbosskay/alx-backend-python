#!/usr/bin/env python3
"""Module function make_multiplier is established"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by another float"""
    return lambda i: i * multiplier
