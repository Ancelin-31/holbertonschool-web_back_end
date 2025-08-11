#!/usr/bin/env python3
# This module provides a helper function for pagination calculations.

def index_range(page: int, page_size: int) -> tuple:
    # Returns a tuple of (start_index, end_index) for pagination.
    # Page numbers are 1-indexed.

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
