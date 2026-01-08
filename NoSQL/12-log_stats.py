#!/usr/bin/env python3
"""12-log_stats.py
Module that provides statistics about the nginx logs in MongoDB
"""

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("localhost", 27017)

# Select the "logs" database and the "nginx" collection
db = client.logs
collection = db.nginx

# Get the total number of logs in the collection
total_logs = collection.count_documents({})

# Count the number of logs for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Count the number of logs where method = GET and path = /status
status_check = collection.count_documents({"method": "GET", "path": "/status"})

# Print the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check} status check")
"""Script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
if __name__ == "__main__": 
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    })
