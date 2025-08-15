#!/usr/bin/env python3
"""Print basic stats about Nginx logs stored in MongoDB."""

if __name__ == "__main__":
    from pymongo import MongoClient


    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"methods": "GET", "path": "/status"})
    print(f"{status_check} status check")

