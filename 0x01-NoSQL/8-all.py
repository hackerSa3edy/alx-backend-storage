#!/usr/bin/env python3
"""List all documents in Python"""
from pymongo import collation


def list_all(mongo_collection: collation):
    """
    Function that lists all documents in a collection.

    Args:
        mongo_collection (collation): The MongoDB collection object.

    Returns:
        All the documents in the collection.
    """
    return mongo_collection.find()
