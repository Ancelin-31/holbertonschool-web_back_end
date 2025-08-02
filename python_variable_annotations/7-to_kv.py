#!/usr/bin/env python3
"""
square with a tuple from str and list
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    square with a tuple from str and list
    """
    return (k, float(v ** 2))
