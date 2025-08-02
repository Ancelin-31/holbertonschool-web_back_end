#!/usr/bin/env python3
"""
return vlaue with type
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return value with type
    """
    return [(i, len(i)) for i in lst]
