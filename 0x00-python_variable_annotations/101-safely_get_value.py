#!/usr/bin/env python3
"""Module function safely_get_value is established"""
from typing import Any, Mapping, Union, TypeVar


TyV = TypeVar('T')
Res = Union[Any, TyV]
Def = Union[TyV, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Getting and returns the value of dict using a specific key"""
    if key in dct:
        return dct[key]
    else:
        return default
