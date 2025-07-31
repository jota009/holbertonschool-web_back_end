# Holberton Web Back‑End Projects Overview

> A curated set of Python mini‑projects to master modern back‑end concepts: static typing, asynchronous programming, and async comprehensions.

---

## 🏗 Repository Structure

```plaintext
holbertonschool-web_back_end/
├── python_variable_annotations/   # PEP 484 & 526: type hints & variable annotations
├── python_async_function/         # asyncio basics: coroutines, tasks, concurrency
├── python_async_comprehension/    # async generators, async for, async comprehensions
└── README.md                      # (this file)
```

---

## 🌟 Projects at a Glance

### 1. **`python_variable_annotations`**

* **Goal:** Learn Python type annotations for functions and variables.
* **Highlights:**

  * Basic function hints: `def add(a: float, b: float) -> float`
  * Complex generics: `List[float]`, `Union[int, float]`, `Callable[[float], float]`
  * Variable annotations: `pi: float = 3.14`
* **Run:** follow that folder’s `README.md` for detailed instructions.

### 2. **`python_async_function`**

* **Goal:** Master `asyncio` coroutines, tasks, and concurrent execution.
* **Highlights:**

  * `async def` & `await`: non‑blocking pauses.
  * `asyncio.create_task()`: scheduling tasks.
  * `asyncio.as_completed()`: process tasks by completion order.
  * Measuring runtimes with `time` module.
* **Run:** open its `README.md` for example commands.

### 3. **`python_async_comprehension`**

* **Goal:** Explore asynchronous generators and async comprehensions.
* **Highlights:**

  * `async for` loops over time‑driven generators.
  * Async list comprehensions: `[x async for x in agen()]`.
  * Parallel streams with `asyncio.gather`.
* **Run:** see that folder’s `README.md` for quickstart.

---

## 🛠 Getting Started

1. **Clone the repo:**

   ```bash
   git clone <repository_url>
   cd holbertonschool-web_back_end
   ```

2. **Explore project folders:**
   Each subdirectory contains its own `README.md` with specific steps.

3. **Python version:**
   Ensure you’re using **Python 3.10+** for full `asyncio` and typing support.

4. **Run examples:**
   In any project folder, make scripts executable (`chmod +x *.py`) and execute the provided mains.

---

## 🤝 Contributing & Next Steps

* Add more exercises (e.g., advanced typing, network I/O).
* Integrate continuous integration with **MyPy** and **pytest**.
* Expand into real‑world adapters: HTTP clients, databases, websockets.

---

**Author:** Josniel Ramos (Holberton School)
