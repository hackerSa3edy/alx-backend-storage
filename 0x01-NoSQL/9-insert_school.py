#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection object.
        **kwargs: Arbitrary keyword arguments representing the fields and
            values of the document to be inserted.

    Returns:
        bson.objectid.ObjectId: The ID of the newly inserted document.
    """
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
