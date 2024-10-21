#!/usr/bin/env python3
"""Change school topics"""
from typing import List
from pymongo import collection


def update_topics(
    mongo_collection: collection,
    name: str,
    topics: List[str]
        ) -> None:

    """
    Function that changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection object.
        name (str): The name of the school document to update.
        topics (List[str]): The list of topics to set for the school document.

    Returns:
        None
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
