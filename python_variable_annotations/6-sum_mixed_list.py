#!/usr/bin/env python3
"""
list of floats and integers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return sum of values in a list
    """
    return sum(mxd_lst)