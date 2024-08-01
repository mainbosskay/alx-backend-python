#!/usr/bin/env python3
"""Module function element_length is established"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates length of a list of sequence"""
    return [(i, len(i)) for i in lst]
