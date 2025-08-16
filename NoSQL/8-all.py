#!/usr/bin/env python3
"""
list all documents
"""


def list_all(mongo_collection):
    """
    list all documents
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
