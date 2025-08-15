#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return all documents as a list (empty list if none)."""
    return list(mongo_collection.find())
