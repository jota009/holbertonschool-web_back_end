#!/usr/bin/env python3
"""Update the topics list for all school docs matching a given name."""


def update_topics(mongo_collection, name, topics):
    """Change the 'topics' of all documents where 'name' matches.

    Args:
        mongo_collection: A PyMongo collection object.
        name: School nam to match (string).
        topics: New list of topics (list of strings).

    Returns:
        The number of modified documents (int).
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
