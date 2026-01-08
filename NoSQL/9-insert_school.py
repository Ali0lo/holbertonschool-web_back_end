#!/usr/bin/env python3
"""Inserts a new document into a MongoDB collection"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a document into mongo_collection using kwargs and returns the new _id"""
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
