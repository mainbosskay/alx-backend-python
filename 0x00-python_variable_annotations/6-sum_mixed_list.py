#!/usr/bin/env python3
"""Module for function sum_mixed_list is established"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of list of int and floats"""
    return float(sum(mxd_lst))
