#!/usr/bin/env python3
"""Lists all documents in a collection."""

from typing import List, Dict
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict]:
    """Return all documents in the collection as a list.
    (or [] if none).

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of documents (dicts). Empty list if none exist.
    """
    return list(mongo_collection.find())
