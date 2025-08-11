#!/usr/bin/env python3
"""Simple pagination based on a csv file"""

import csv
from typing import List
import os


DATA_DIR = os.path.dirname(__file__)

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = os.path.join(DATA_DIR, "Popular_Baby_Names.csv")

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
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
