#!/usr/bin/env python3
"""
Change all topics of a document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Change all topics
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
