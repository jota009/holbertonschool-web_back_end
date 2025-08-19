# 🗄️ NoSQL & MongoDB — Study + Task Guide

A friendly, visual walkthrough of NoSQL concepts and the exact MongoDB patterns you’ve used in the Holberton tasks — with tiny examples, checklists, and gotchas.

---

## 📚 What is “NoSQL”?

**Not a framework.** It’s an umbrella term for **non‑relational** databases.

| Family          | Examples          | Data model                         | Typical use                           |
| --------------- | ----------------- | ---------------------------------- | ------------------------------------- |
| **Document**    | MongoDB, CouchDB  | JSON/BSON documents in collections | Product catalogs, user profiles, logs |
| **Key‑Value**   | Redis, DynamoDB   | Simple key→value                   | Caches, counters, ephemeral data      |
| **Wide‑Column** | Cassandra, HBase  | Rows with flexible columns         | High‑write, time‑series               |
| **Graph**       | Neo4j, JanusGraph | Nodes + edges                      | Relationships, recommendations        |

> Think **MongoDB** as: **Databases → Collections → Documents** (JSON‑like, flexible).

---

## 🧭 When to prefer MongoDB (Document DB)

* ✅ Evolving or flexible schemas (fields vary per record)
* ✅ Nested data (arrays/objects) you want to store “as is”
* ✅ High write throughput, horizontal scaling patterns
* ⚠️ Heavy relational joins → a relational DB (Postgres/MySQL/SQLite) may fit better

---

## 🧱 MongoDB mental model

* **Database**: container (e.g., `logs`, `my_db`)
* **Collection**: table‑like group (e.g., `nginx`, `school`)
* **Document**: JSON‑like record (BSON under the hood)
* **BSON**: Binary JSON with extra types (e.g., `ObjectId`)

---

## 🛠️ Tooling you’ll see

* **Server**: `mongod` (the database process)
* **Shells**:

  * Legacy: `mongo` (used by the checker’s examples)
  * Modern: `mongosh` (use this locally; supports `--file` / `--eval`)
* **Python driver**: `pymongo` (v4.x)

---

## 📝 Holberton “MongoDB Command File” rules

For files like `0-list_databases`, `2-insert`, etc.

* Line 1 **must be a comment**: `// my comment`
* End the file with a **newline**
* Run DB selection from CLI (don’t write `use my_db` inside the file)
* Run it:

  * Legacy style: `mongo my_db < NoSQL/3-all`
  * Modern: `mongosh --quiet "mongodb://127.0.0.1:27017/my_db" < NoSQL/3-all`

**Common pitfalls**

* Wrong first line (missing `//`)
* No newline at end of file
* Windows CRLF endings (`^M`) → use `dos2unix file`

---

## 🍰 Shell mini‑recipes (used in tasks)

```js
// list DBs
show dbs

// insert one document (legacy syntax used by checker)
db.school.insert({ name: "Holberton school" })

// list all documents
db.school.find({})

// match by field
db.school.find({ name: "Holberton school" })

// count all documents
db.school.count()

// update *all* matches → set new field/value
db.school.update(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } },
  { multi: true }
)

// delete all matches
db.school.deleteMany({ name: "Holberton school" })
```

> Tip: In `mongosh` non‑interactive mode, `find()` returns a cursor and may print nothing. Use: `db.school.find({}).forEach(doc => printjson(doc))` to force output.

---

## 🐍 PyMongo patterns (Python tasks)

(Use these shapes from memory; no prints inside your functions.)

```python
#!/usr/bin/env python3
"""PyMongo CRUD patterns used in the project."""

# List all documents
def list_all(mongo_collection):
    """Return all documents as a list (empty list if none)."""
    return list(mongo_collection.find())

# Insert document from kwargs, return _id
def insert_school(mongo_collection, **kwargs):
    """Insert and return inserted _id."""
    return mongo_collection.insert_one(dict(kwargs)).inserted_id

# Update all docs by name → set topics
def update_topics(mongo_collection, name, topics):
    """Set 'topics' list for all docs where name matches."""
    res = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return res.modified_count

# Find schools where 'topics' array contains topic
def schools_by_topic(mongo_collection, topic):
    """Return list of docs whose 'topics' contains the topic."""
    return list(mongo_collection.find({"topics": topic}))
```

---

## 📊 Exact‑format script: Nginx log stats (`12-log_stats.py`)

Prints **exact** lines; note the **TAB** before each method line.

```python
#!/usr/bin/env python3
"""Print basic stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats() -> None:
    """Print total logs, per-method counts, and /status count."""
    col = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(f"{col.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {col.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {col.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {col.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {col.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {col.count_documents({'method': 'DELETE'})}")
    print(f"{col.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    log_stats()
```

**Gotchas the checker enforces**

* The header must be exactly `Methods:`
* Each method line begins with a **TAB** (`\t`), not spaces
* Method order must be: GET, POST, PUT, PATCH, DELETE

---

## 🧪 Local data: restore the sample dump

```bash
curl -o dump.zip -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip"
unzip dump.zip
mongorestore dump
# Data ends up in DB 'logs', collection 'nginx'
```

---

## 🧰 Troubleshooting checklist

* **Shell mismatch**: `mongo` vs `mongosh`. Use `mongosh` locally:

  * `mongosh --quiet "mongodb://127.0.0.1:27017/my_db" --file NoSQL/3-all`
* **Command file fails**: ensure first line is `// my comment` + final newline.
* **No output for find() with mongosh**: add `.forEach(doc => printjson(doc))`.
* **PEP8 (pycodestyle) errors**: ensure **two blank lines** before top‑level `def`.
* **VS Code shows missing `pymongo`**: select the interpreter with PyMongo or `python3 -m venv .venv && source .venv/bin/activate && pip install pymongo==4.8.0`.
* **Windows line endings**: run `dos2unix` on command files.

---

## 🧠 Quick drills (write from memory)

1. Write `insert_school` that returns the `_id`.
2. Write `schools_by_topic` using `{ "topics": topic }`.
3. Write a command file that updates all schools named X to add `{ city: "PR" }`.
4. Write the five “method” lines of `12-log_stats.py` with a TAB prefix.

---

## 📖 Glossary

* **Document**: JSON‑like record (BSON in storage)
* **Collection**: group of documents (like a table)
* **\_id/ObjectId**: primary key (unique identifier)
* **\$set**: MongoDB update operator to set/replace a field
* **Cursor**: iterable result of `find()`, convert to list if needed

---

## Author: Josniel Ramos
