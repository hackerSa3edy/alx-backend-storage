#!/usr/bin/env python3
"""Get top students sorted by average score"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection object.

    Returns:
        List[dict]: A list of student documents sorted by their average
            score in descending order.
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                },
                'topics': 1
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
