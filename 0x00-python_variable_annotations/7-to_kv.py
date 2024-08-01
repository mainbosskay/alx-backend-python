#!/usr/bin/env python3
"""Module for function to_kv is established"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key and value to a tuple of the key and the value squared"""
    return (k, float(v**2))
