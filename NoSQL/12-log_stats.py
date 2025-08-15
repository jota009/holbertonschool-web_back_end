#!/usr/bin/env python3
"""Print basic stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats() -> None:
    """Print total logs, per-method counts, and /status count."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")

    # EXACT header and TAB before each method line
    print("Methods:")
    print(f"\tmethod GET: {col.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {col.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {col.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {col.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {col.count_documents({'method': 'DELETE'})}")

    status_count = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    client.close()


if __name__ == "__main__":
    log_stats()
