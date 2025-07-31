# Python Variable Annotations

> A mini-project to learn and practice Python type hints and variable annotations.

---

## 📚 Topics Covered

1. **Basic Function Annotations**

   * `add(a: float, b: float) -> float` – adding two floats
   * `concat(str1: str, str2: str) -> str` – concatenating two strings
   * `floor(n: float) -> int` – computing the mathematical floor of a float
   * `to_str(n: float) -> str` – converting a float to its string representation

2. **Variable Annotations**

   * Declaring typed globals:

     ```python
     a: int = 1
     pi: float = 3.14
     i_understand_annotations: bool = True
     school: str = "Holberton"
     ```

3. **Complex Types with `typing`**

   * **Lists of floats**: `sum_list(input_list: List[float]) -> float`
   * **Mixed lists**: `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`
   * **Key-Value tuples**: `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`
   * **Higher-order functions**: `make_multiplier(multiplier: float) -> Callable[[float], float]`

4. **Duck Typing & Iterables**

   * Annotating generic iterables of sequences:

     ```python
     def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]
     ```

---

## 🛠 Getting Started

1. **Clone the repository** and navigate to the `python_variable_annotations/` directory.
2. **Make scripts executable**:

   ```bash
   chmod +x *.py
   ```
3. **Run each test harness** to verify functionality and annotations:

   ```bash
   ./0-main.py  # add
   ./1-main.py  # concat
   # ... up to 9-element_length
   ```

---

## 🔍 Key Concepts

### Type Hints (PEP 484)

* Annotate function parameters and return values.
* Improves readability and enables static checking with tools like `mypy`.

### Variable Annotations (PEP 526)

* Annotate module-level variables to declare expected types.

### The `typing` Module

* **Generic Types**: `List[T]`, `Tuple[T1, T2]`
* **Unions**: `Union[A, B]`
* **Callables**: `Callable[[ArgTypes], ReturnType]`
* **Iterables & Sequences**: `Iterable[T]`, `Sequence`

### Static Analysis

* Use **`mypy`** or editor integrations to catch type mismatches before runtime.

---

## 🚀 Next Steps

* Explore more generics: `Dict[str, Any]`, `Optional[T]`.
* Integrate `mypy` into your CI pipeline for automated type checking.
* Practice annotating real-world modules and services.

---

**Author:** Josniel Ramos (Holberton School)
