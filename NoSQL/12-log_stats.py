#!/usr/bin/env python3
"""
Module that provides stats about Nginx logs stored in MongoDB
"""


if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the logs database and nginx collection
    db = client.logs
    collection = db.nginx

    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Display methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get status check count (method=GET and path=/status)
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
