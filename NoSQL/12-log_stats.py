#!/usr/bin/env python3
"""Print basic stats about Nginx logs stored in MongoDB."""


from pymongo import MongoClient


def log_stats() -> None:
    """Print total logs, per-method counts and /status checks."""
    client = MongoClient("mongodb://127.0.01:27017")
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    get_cnt = col.count_documents({"method": "GET"})
    post_cnt = col.count_documents({"method": "POST"})
    put_cnt = col.count_documents({"method": "PUT"})
    patch_cnt = col.count_documents({"method": "PATCH"})
    delete_cnt = col.count_documents({"method": "DELETE"})
    print(f"\tmethod GET: {get_cnt}")
    print(f"\tmethod POST: {post_cnt}")
    print(f"\tmethod PUT: {put_cnt}")
    print(f"\tmethod PATCH: {patch_cnt}")
    print(f"\tmethod DELETE: {delete_cnt}")

    status_count = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    client.close()

    if __name__ == "__main__":
        log_stats()
