# Async Comprehension Project

> Dive into Python’s async generators and comprehensions to process data streams non‑blocking.

---

## 📚 Topics Covered

1. **Asynchronous Generators** (`0-async_generator.py`)

   * Declared with `async def`
   * `await asyncio.sleep(1)` before each `yield`
   * Yields 10 random floats between 0 and 10 at 1‑second intervals

2. **Async Comprehensions** (`1-async_comprehension.py`)

   * Collect values from an async generator in one line
   * Syntax: `[value async for value in async_generator()]`

3. **Parallel Execution with `asyncio.gather`** (`2-measure_runtime.py`)

   * Run multiple async comprehensions concurrently
   * Measure total runtime (\~10 s for four parallel runs)

---

## 🗂 File Overview

| File                       | Purpose                                                              |
| -------------------------- | -------------------------------------------------------------------- |
| `0-async_generator.py`     | `async_generator()` yields 10 random floats, pausing 1 s each time   |
| `1-async_comprehension.py` | `async_comprehension()` gathers values from `async_generator`        |
| `2-measure_runtime.py`     | `measure_runtime()` runs four parallel comprehensions and times them |

---

## 🚀 Getting Started

1. **Navigate** into this folder:

   ```bash
   cd python_async_comprehension
   ```
2. **Grant execute** permission:

   ```bash
   chmod +x *.py
   ```
3. **Run tests**:

   ```bash
   ./0-main.py    # async generator output
   ./1-main.py    # async comprehension output
   ./2-main.py    # runtime measurement (~10 s)
   ```

---

## 🔍 Key Concepts

* **`async def` & `yield`**: build non-blocking data streams.
* **`async for`**: consume async iterators.
* **Async comprehensions**: concise, await-enabled list constructions.
* **Concurrency**: `asyncio.gather` runs awaitables in parallel.

---

## ⚙️ Next Steps

* Handle errors inside async generators and comprehensions.
* Explore cancellation (`.cancel()`) and timeouts.
* Integrate real I/O streams (e.g., websockets, file readers).

---

**Author:** Josniel Ramos (Holberton School)
