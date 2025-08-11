#!/usr/bin/env python3
"""Simple helper function for pagination."""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple (start, end) of 0-based indices for slicing.

    - `page` is 1-indexed (page 1 is the first page).
    - `start` is inclusive; `end` is exclusive (Python slicing style).
      e.g. my_list[start:end]

    Examples (for your own checks, not required in code):
      page=1, page_size=7   -> (0, 7)
      page=3, page_size=15  -> (30, 45)
    """

    offset = (page - 1) * page_size
    start = offset
    end = start + page_size

    return (start, end)
