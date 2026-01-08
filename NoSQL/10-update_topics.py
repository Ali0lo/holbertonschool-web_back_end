#!/usr/bin/env python3
"""Updates the topics of a school document based on the name"""

def update_topics(mongo_collection, name, topics):
    """Updates all documents with the given school name, setting the topics field"""
    if mongo_collection is None:
        return
    mongo_collection.update_many(
        {"name": name},
        {"\$set": {"topics": list(topics)}}
    )
"""
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
        mongo_collection: pymongo collection object
        name (string): the school name to update
    """
    mongo_collection. update_many(
        {"name": name},
    )
