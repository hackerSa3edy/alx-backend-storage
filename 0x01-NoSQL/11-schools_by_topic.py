#!/usr/bin/env python3
"""Filter based on topic"""
from typing import List
from pymongo import collection


def schools_by_topic(mongo_collection: collection, topic: str) -> List:
    """
    Function that returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection object.
        topic (str): The topic to filter schools by.

    Returns:
        List: A list of school documents that have the specified topic.
    """
    return mongo_collection.find({'topics': topic})
