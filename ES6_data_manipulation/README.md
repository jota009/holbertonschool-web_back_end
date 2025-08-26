# ES6 Data Manipulation

> A friendly, visual guide to working with modern JavaScript data: arrays, sets, maps, iterables, typed arrays, and more. Built around the Holberton **ES6\_data\_manipulation** tasks with cheat‑sheets, patterns, and real‑world tips.

---

## 🎯 Learning Goals

* Choose the right tool: **map**, **filter**, **reduce**, **find**, **some/every**
* Keep code **pure & predictable**: avoid mutations; use **spread** & **rest**
* Use **Set**/**Map** for performance and clarity
* Work with **Typed Arrays**/**DataView** for binary data
* Build readable **pipelines** and small utility functions

---

## ⚙️ Setup (Quick)

```bash
cd ES6_data_manipulation
npm install
npm run dev -- 0-main.js   # run a specific task demo
npm test                    # if tests are provided
npm run lint                # lint the project
```

---

## 🧱 Core Concepts (Cheat‑Sheet)

### Arrays — Transform • Select • Summarize

* **map**: 1→1 transform
* **filter**: select subset
* **reduce**: many→one (sum, index, group)
* **find / some / every**: query answers
* **sort**: give a comparator `(a,b)=>a-b` for numbers; `localeCompare` for strings

```js
const ids = students.map(s => s.id);
const sf = students.filter(s => s.location === 'San Francisco');
const idSum = students.reduce((sum, { id }) => sum + id, 0);
const hasColumbia = students.some(s => s.location === 'Columbia');
const firstId5 = students.find(s => s.id === 5);
```

### Immutability & Copying

* Avoid mutating inputs; return **new** arrays/objects
* **Object spread**: `{ ...obj, updated: true }`
* **Array spread**: `[...arr, item]`
* Mutating vs non‑mutating (prefer right side):

  * Mutate: `push`, `pop`, `splice`, `sort`, `reverse`
  * Safe: `concat`/spread, `slice`, `filter`, `map`, `copy before sort`

### Rest & Destructuring

```js
const [first, ...rest] = arr;
const { id, ...others } = student;
```

### Set — Uniqueness & Membership

* Build: `new Set(array)`  → de‑dupe, keep order
* Check: `set.has(value)` (O(1))
* Convert back: `[...set]` / `Array.from(set)`
* Set ops:
  `union = new Set([...A, ...B])`
  `inter = new Set([...A].filter(x => B.has(x)))`

### Map — Keyed Data

* Any type as key, preserves insertion order
* `set/get/has/size` & easy iteration: `for (const [k,v] of map)`
* Convert: `Object.fromEntries(map)` ⇆ `new Map(Object.entries(obj))`

### Iterables & Entries

* Use `for...of` on arrays, sets, maps
* Helpful views: `arr.entries()`, `arr.keys()`, `arr.values()`

### Typed Arrays & DataView (Binary)

* `ArrayBuffer`: raw bytes
* `DataView`: flexible reads/writes, endianness control
* `setInt8(offset, value)` / `getInt8(offset)`; check bounds

---

## 🧩 Task‑by‑Task Highlights

### 0) **getListStudents** → array of student objects

* Models your base dataset for later tasks.

### 1) **getListStudentIds** → map to IDs

* Guard non‑arrays; `map` for projection.

### 2) **getStudentsByLocation** → filter by city

* `filter` with `({ location }) => location === city`.

### 3) **getStudentIdsSum** → reduce to sum

* Seed with `0`; `reduce((sum,{id}) => sum + id, 0)`.

### 4) **updateStudentGradeByCity** → filter + map (+ lookup)

* Build `gradeById = new Map(newGrades.map(({studentId, grade}) => [studentId, grade]))`
* `filter` by city → `map` add `grade: map.get(id) ?? 'N/A'`

### 5) **createInt8TypedArray** → DataView write

* Bounds check; allocate `ArrayBuffer` → `DataView` → `setInt8`.

### 6) **setFromArray** → new Set

* `return new Set(array)`; duplicates removed.

### 7) **hasValuesFromArray** → membership ALL

* `return array.every(v => set.has(v))`.

### 8) **cleanSet** → join suffixes of prefixed values

* Guard empty prefix → iterate set → `startsWith(prefix)` → `slice(prefix.length)` → `join('-')`.

*(Add later tasks here similarly if your project includes them: groceries list, update unique items, weak map counters.)*

---

## 🛠️ Patterns & Recipes

### Filter → Map (enrich subset)

```js
const results = list
  .filter(x => keep(x))
  .map(x => ({ ...x, grade: calc(x) }));
```

### Reduce to a grouped object

```js
const byCity = students.reduce((acc, s) => {
  (acc[s.location] ||= []).push(s);
  return acc;
}, {});
```

### Fast lookups (Map & Set)

```js
const byId = new Map(students.map(s => [s.id, s]));
const idSet = new Set(students.map(s => s.id));
```

### Locale & numeric sort

```js
const numsAsc = [...nums].sort((a,b) => a - b);
const alpha = [...names].sort((a,b) => a.localeCompare(b));
```

---

## 🧪 Debugging & Checker Tips

* Guard inputs (`Array.isArray`, `instanceof Set/Map`)
* Don’t mutate parameters (`no-param-reassign`)
* Use the exact error text when specified (e.g., `'Position outside range'`)
* Provide a comparator for numeric `sort`
* Prefer `??` over `||` for numeric `0` or empty strings
* Return exactly what the task expects (DataView vs ArrayBuffer, Set vs Array)

---

## 💡 Real‑World Use Cases

* **Analytics**: filter cohorts, map fields, reduce to KPIs
* **Access control**: `Set` for roles/permissions checks
* **Join datasets**: `Map` by `id` to enrich lists
* **Binary I/O**: parse file headers or protocol frames with `DataView`

---

## 📝 Mini‑Quizzes (lock it in)

1. Why seed `reduce` with `0`? What happens without it on empty arrays?
2. When do you prefer `Set` over `Array.includes`?
3. Why use `?? 'N/A'` instead of `|| 'N/A'` for grades?
4. What’s the complexity of `array.every(v => set.has(v))`?

**Answers**

1. Avoids errors and sets the correct type; without seed, empty arrays throw and the first element becomes the accumulator.
2. Large membership checks; `Set.has` is O(1) vs O(n) for arrays.
3. `??` only falls back for `null/undefined`—keeps `0` as a valid grade.
4. O(n) with early exit on first missing value.

---

## 📚 Reference Snippets

```js
// groupBy key
const groupBy = (arr, key) => arr.reduce((a, x) => ((a[x[key]] ||= []).push(x), a), {});

// unique values
const unique = (arr) => [...new Set(arr)];

// index by id
const indexById = (arr) => new Map(arr.map(x => [x.id, x]));

// safe numeric sort
const sortNumAsc = (arr) => [...arr].sort((a,b) => a - b);
```

---

## ✅ Study Checklist

* [ ] I can explain map/filter/reduce and choose the right one
* [ ] I know which methods mutate vs return new arrays
* [ ] I can use Set/Map and convert to/from arrays/objects
* [ ] I can chain filter→map→reduce without side effects
* [ ] I can read/write bytes with DataView (setInt8/getInt8)
* [ ] I handle edge cases: empty arrays, missing grades, empty prefixes

---

## 👤 Author

**Josniel Ramos** — Software Engineering Student, Holberton School

> Tip: When stuck, apply the 5‑step recipe: **Output type → Guards → Lookups → Pipeline → Assemble**. It’s the fastest way to break down any data task.
