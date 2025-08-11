#!/usr/bin/env python3
"""Hypermedia pagination on top of simple pagination."""


import csv
import math
from typing import List, Dict, Any
import os

index_range = __import__('0-simple_helper_function').index_range


DATA_DIR = os.path.dirname(__file__)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = os.path.join(DATA_DIR, "Popular_Baby_Names.csv")

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        assert isinstance(page, int) and page > 0, "page must be an int > 0"
        assert isinstance(page_size, int
                          ) and page_size > 0, "page_size must be an int > 0"

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return hypermedia pagination info."""
        data = self.get_page(page, page_size)          # reuse get_page
        actual_size = len(data)                        # length of THIS page
        total_items = len(self.dataset())              # whole dataset
        total_pages = math.ceil(total_items / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": actual_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
