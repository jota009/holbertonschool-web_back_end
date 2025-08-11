#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset: Dict[int, List] = None

    def dataset(self) -> List[List]:
        """Cached dataset (list of rows without header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # drop header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            data = self.dataset()
            # Index the entire dataset: 0..len(data)-1
            self.__indexed_dataset = {i: row for i, row in enumerate(data)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient page starting at `index`."""
        if index is None:
            index = 0

        # Guards
        assert isinstance(index, int), "index must be an int"
        assert isinstance(page_size, int
                          ) and page_size > 0, "page_size must be an int > 0"
        assert 0 <= index < len(self.dataset()), "index out of range"

        idx_map = self.indexed_dataset()
        data: List[List] = []
        cursor = index
        upper_bound = len(self.dataset())

        # Collect up to `page_size` existing rows, skipping deleted indices
        while len(data) < page_size and cursor < upper_bound:
            if cursor in idx_map:
                data.append(idx_map[cursor])
            cursor += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),  # actual size of this page
            "next_index": cursor,    # first index after the last returned item
        }
