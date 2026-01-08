#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def main():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    # Count total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
