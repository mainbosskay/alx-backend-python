#!/usr/bin/env python3
"""Module function safe_first_element is established"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Getting and return the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
