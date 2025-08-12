# 📚 Pagination — Holberton Web Back End

Master the three pillars of pagination: **page/size**, **hypermedia metadata**, and **deletion‑resilient paging**. This project uses a real CSV dataset (NYC Popular Baby Names) to practice production‑style pagination patterns.

---

## 🎯 Learning Objectives

By the end of this project, you can explain (without Google):

* **Simple pagination** with `page` and `page_size` (offset math and slicing).
* **Hypermedia pagination** that returns navigation metadata (self‑describing API).
* **Deletion‑resilient pagination** that avoids skips/duplicates after rows are removed.

---

## 🧭 Project Overview

You’ll build a small pagination toolkit over a CSV dataset:

* `index_range(page, page_size)` → returns **(start, end)** indices.
* `Server.get_page(page, page_size)` → returns a **list of rows** for that page.
* `Server.get_hyper(page, page_size)` → wraps `get_page` with **hypermedia** info:

  * `page_size` (actual length of the returned page)
  * `page`, `data`, `next_page`, `prev_page`, `total_pages`
* `Server.get_hyper_index(index, page_size)` → **deletion‑resilient**:

  * Starts at `index`, **skips holes**, returns up to `page_size` items
  * Also returns `next_index` for the next call

> **Repo:** `holbertonschool-web_back_end`
> **Directory:** `pagination`

---

## 🗂️ Structure

```
pagination/
├─ 0-simple_helper_function.py      # index_range
├─ 1-simple_pagination.py           # Server.get_page
├─ 2-hypermedia_pagination.py       # Server.get_hyper
├─ 3-hypermedia_del_pagination.py   # Server.get_hyper_index
├─ Popular_Baby_Names.csv           # dataset (≈19k rows, header removed in code)
├─ 0-main.py 1-main.py 2-main.py 3-main.py   # sample runners
└─ README.md
```

---

## 🔑 Key Concepts (Exam Quick‑Look)

### 1) Page/Size (Offset) Pagination

* **Pages are 1‑indexed** (page 1 is the first page).
* **Offset formula:** `offset = (page - 1) * page_size`.
* Slice lists using **\[start\:end)** (end is exclusive).
* Validate inputs: `page`, `page_size` are **int > 0** (use `assert`).

### 2) Hypermedia Pagination

Return navigation data so the client knows where to go next:

* `page_size` = `len(data)` (actual items on this page, may be 0 on empty pages).
* `next_page` = `page + 1` **iff** `page < total_pages`, else `None`.
* `prev_page` = `page - 1` **iff** `page > 1`, else `None`.
* `total_pages` = `ceil(total_items / page_size)`.

### 3) Deletion‑Resilient Pagination

* Build an **index → row** map (e.g., `{0: row0, 1: row1, ...}`).
* Given `index` + `page_size`, **scan forward**, collecting only indices that still exist.
* Return:

  * `index` (the requested start)
  * `data` (up to `page_size` rows)
  * `page_size` = `len(data)`
  * `next_index` = first index **after** the last returned item
* Even if some indices were deleted between calls, the **user won’t miss items**.

---

## ▶️ How to Run

1. Place `Popular_Baby_Names.csv` in the `pagination/` folder.
   Sanity check: `wc -l Popular_Baby_Names.csv` → should be **19419** (including header).

2. Run the sample mains:

```bash
python3 0-main.py   # tests index_range
python3 1-main.py   # tests get_page + assertions + empty-page behavior
python3 2-main.py   # tests hypermedia fields & counts
python3 3-main.py   # tests deletion-resilient pagination
```

> **Tip:** If you see XML in the CSV, re‑download — S3 presigned links can expire.

---

## 🧪 Acceptance Checklist

* [ ] `index_range` returns correct `(start, end)` for any valid `page`, `page_size`.
* [ ] `get_page`:

  * [ ] Uses `assert` to enforce `int > 0` for inputs.
  * [ ] Uses `index_range` for bounds.
  * [ ] Returns `[]` if `start >= len(dataset)`.
* [ ] `get_hyper`:

  * [ ] Wraps `get_page`.
  * [ ] `page_size` equals `len(data)` (not the requested size).
  * [ ] Correct `next_page`, `prev_page`, `total_pages`.
* [ ] `get_hyper_index`:

  * [ ] Uses `index` default **0** when `None`.
  * [ ] Asserts `0 <= index < len(dataset)`.
  * [ ] Skips missing indices and returns `next_index` properly.

---

## 🧠 Edge Cases You Should Expect

* **Empty page**: page beyond data → `data = []`, `page_size = 0`, `next_page = None`.
* **Last page shorter than requested**: valid; `len(data)` may be < `page_size`.
* **After deletions**: `get_hyper_index` still returns the next contiguous items.
* **Large page numbers**: offset may exceed list length → return `[]` (no crash).

---

## 🛣️ What This Enables (Real‑World Use)

* **Catalogs / listings** (e.g., places, products) with stable **page‑number** UIs.
* **Activity feeds / reviews** using **deletion‑resilient** or **cursor** approaches.
* **Admin tables** with predictable navigation and accessible controls.

---

## 🙋🏽‍♂️ FAQ

* **Why is the end index exclusive?**
  Python slicing uses `[start:end)` which makes ranges easy to chain and combine.

* **Why not always compute `total_pages`?**
  On very large datasets, counting can be expensive. It’s fine to omit or cache it in real systems.

* **Why assert against `len(dataset)` for deletion‑resilient?**
  It sets a safe **upper bound**; your indexed map may shrink after deletions.

---

## ✍️ Author

**Josniel Ramos**
