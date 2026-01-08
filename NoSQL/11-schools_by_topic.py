#!/usr/bin/env python3
"""Returns a list of schools having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """Returns all documents where topics list contains the given topic"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
