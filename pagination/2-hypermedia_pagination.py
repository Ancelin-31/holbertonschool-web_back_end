#!/usr/bin/env python3
"""This module provides a helper function for pagination calculations."""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of (start_index, end_index) for pagination.
    Page numbers are 1-indexed."""

    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset"""

        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset as dictionaries"""

        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        data = dataset[start:end]
        total_pages = math.ceil(len(dataset) / page_size)

        hyper = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if end < len(dataset) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper
