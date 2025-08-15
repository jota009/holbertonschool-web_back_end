#!/usr/bin/env python3
"""Find schools by topic in a MongoDB collection."""


def schools_by_topic(mongo_collection, topic):
    """Retunr all school documents that inlcude a given topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic: Topic string to search for in the 'topics' array.

    Returns:
        List of documents whose 'topics' contains the given topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
