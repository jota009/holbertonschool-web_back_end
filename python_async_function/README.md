# Python AsyncIO Essentials

> A mini-project exploring Python’s `asyncio` library through practical coroutine and task patterns.

---

## 📚 Topics Covered

1. **Basic Asynchronous Syntax**

   * Defining `async def` coroutines
   * Using `await asyncio.sleep(...)` to pause without blocking
   * Running top‑level coroutines with `asyncio.run()`

2. **Concurrent Coroutines**

   * Spawning multiple coroutines with `asyncio.create_task()`
   * Collecting results as they complete via `asyncio.as_completed()`
   * Achieving first‑done ordering without manual sorting

3. **Measuring Runtime**

   * Timing coroutine execution with the `time` module
   * Calculating average latency per task
   * Comparing concurrent vs. sequential performance

4. **Task Creation & Management**

   * Wrapping coroutines in `asyncio.Task` objects
   * Scheduling tasks immediately from synchronous code
   * Inspecting and canceling tasks if needed

5. **Task Orchestration**

   * Building higher‑level routines that spawn and await tasks
   * Layering abstractions: swapping coroutine factories
   * Real‑world patterns for responsive I/O-bound workloads

---

## 🗂 File Overview

| File                         | Description                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| `0-basic_async_syntax.py`    | `wait_random(max_delay)` coroutine: sleeps for a random float delay and returns it.                    |
| `1-concurrent_coroutines.py` | `wait_n(n, max_delay)`: runs `n` random waits concurrently, returns delays in completion order.        |
| `2-measure_runtime.py`       | `measure_time(n, max_delay)`: measures total runtime of `wait_n` and returns average per task.         |
| `3-tasks.py`                 | `task_wait_random(max_delay)`: synchronous function that schedules `wait_random` as an `asyncio.Task`. |
| `4-tasks.py`                 | `task_wait_n(n, max_delay)`: uses `task_wait_random` to spawn and collect `n` tasks concurrently.      |

---

## 🛠 Getting Started

1. **Clone the repository** and navigate to `python_async_function/`:

   ```bash
   git clone <repo_url>
   cd holbertonschool-web_back_end/python_async_function
   ```
2. **Make scripts executable**:

   ```bash
   chmod +x *.py
   ```
3. **Run each example** to see it in action:

   ```bash
   ./0-basic_async_syntax.py    # run via test harness: 0-main.py
   ./1-concurrent_coroutines.py # run via test harness: 1-main.py
   ./2-measure_runtime.py       # run via test harness: 2-main.py
   ./3-tasks.py                 # run via test harness: 3-main.py
   ./4-tasks.py                 # run via test harness: 4-main.py
   ```

---

## 🔍 Key Concepts & Patterns

* **`async def`** / **coroutines**: declare non-blocking functions that return coroutine objects.
* **`await`**: pause a coroutine, yielding control to the event loop.
* **`asyncio.run()`**: entry point for running a coroutine from sync code.
* **`asyncio.create_task()`**: schedule a coroutine as a `Task` immediately.
* **`asyncio.as_completed()`**: iterate futures as they finish, enabling natural ordering by completion time.
* **Timing and measurement**: use `time.time()` or `time.perf_counter()` to benchmark async flows.

---

## 🚀 Real-World Applications

* **Web scraping & HTTP APIs**: fire off many requests concurrently and process responses as soon as they arrive.
* **IoT sensor polling**: poll multiple devices in parallel, handle fastest replies first.
* **Background workers**: schedule cleanup jobs, health checks, or message consumers without blocking main thread.

---

## ⚙️ Next Steps

* **`asyncio.gather`**: batch-await multiple coroutines and collect all results.
* **Error handling**: manage exceptions in tasks and coroutines.
* **Cancellation**: gracefully cancel tasks using `task.cancel()` and handle `asyncio.CancelledError`.
* **Advanced concurrency**: explore `Semaphore`, `Queue`, and `Event` for coordination.

---

**Author:** Josniel Ramos (Holberton School)
