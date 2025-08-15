#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection using kwargs."""


from bson.objectid import ObjectId
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> ObjectId:
    """Insert a new document and return its ObjectId.

    Args:
        mongo_collection: A PyMongo collection object.
        **kwargs: Fields to insert into the document.

    Returns:
        The inserted document's_id (ObjectId).
    """
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id

