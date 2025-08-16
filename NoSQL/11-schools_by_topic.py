#!/usr/bin/env python3
"""
Returns a list of a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
