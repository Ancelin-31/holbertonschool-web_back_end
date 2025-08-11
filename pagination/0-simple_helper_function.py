#!/usr/bin/env python3
# This module provides a helper function for pagination calculations.
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    # Returns a tuple of (start_index, end_index) for pagination.
    # Page numbers are 1-indexed.

    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
