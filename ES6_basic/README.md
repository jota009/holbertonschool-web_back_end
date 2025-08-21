# ES6 Basics

> A clean, friendly guide to the essentials of modern JavaScript (ES6) using the **ES6\_basic** tasks from the Holberton web back end curriculum.

---

## 🎯 Goal of This Repo

Build practical muscle memory with core ES6 features—**variables, functions, objects, modules, and iteration**—so you can write cleaner, safer, and more expressive JavaScript.

---

## 🧭 Quick Start

```bash
# From the project root
cd ES6_basic

# Run an exercise entry file
npm run dev 11-main.js
```

> ✅ Tip: Each task usually pairs an implementation file (e.g., `11-createEmployeesObject.js`) with a small `*-main.js` runner.

---

## 📁 Project Structure (high level)

```
ES6_basic/
├─ 5-spread-operator.js
├─ 10-loops.js
├─ 11-createEmployeesObject.js
├─ 12-createReportObject.js
└─ ...other task files
```

---

## 🧠 ES6 Concepts You’ll Use (with mini examples)

### 1) `let` & `const` (block‑scoped)

```js
const PI = 3.14; // cannot be reassigned (but objects can still have properties changed)
let count = 0;   // can be reassigned; scoped to the nearest block
```

### 2) Arrow Functions

```js
const add = (a, b) => a + b;           // concise return
const greet = name => `Hi, ${name}!`;  // 1 param → no parentheses needed
```

### 3) Template Literals

```js
const tool = 'ESLint';
console.log(`Use ${tool} to keep style consistent.`);
```

### 4) Default Params, Rest, Spread

```js
// default param
function power(base, exp = 2) { return base ** exp; }

// rest: gather many args into an array
function sum(...nums) { return nums.reduce((a, n) => a + n, 0); }

// spread: expand arrays/objects
const a = [1, 2];
const b = [3, 4];
const ab = [...a, ...b]; // [1,2,3,4]
```

### 5) Destructuring

```js
const user = { id: 1, name: 'Ada', role: 'dev' };
const { name, role } = user; // pulls properties into variables
```

### 6) Enhanced Object Literals

* **Computed keys** & **method shorthand**

```js
const key = 'engineering';
const report = {
  [key]: ['Bob', 'Jane'], // computed property name
  getCount(obj) {         // method property shorthand
    return Object.keys(obj).length;
  },
};
```

### 7) Modules (ESM)

```js
// 11-createEmployeesObject.js
export default function createEmployeesObject(departmentName, employees) {
  return { [departmentName]: employees };
}

// 11-main.js
import createEmployeesObject from './11-createEmployeesObject.js';
console.log(createEmployeesObject('Software', ['Bob', 'Sylvie']));
```

### 8) Iteration: `for...of`, `.entries()`, vs `for...in`

```js
const arr = ['a', 'b'];
for (const v of arr) { /* values */ }
for (const [i, v] of arr.entries()) { /* index & value */ }
// for...in iterates enumerable keys (use with objects, not arrays)
```

---

## 🧪 Task Highlights (what you practiced)

### ✅ Task 10 — Loops without mutating params

**File:** `10-loops.js`

**Goal:** prepend a string to each array value and **return a new array** (don’t mutate the parameter).

```js
export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const value of array) {
    result.push(`${appendString}${value}`);
  }
  return result;
}
```

> Why? Linters often enable **no-param-reassign**, discouraging mutation of function parameters.

---

### ✅ Task 11 — Dynamic object keys (computed properties)

**File:** `11-createEmployeesObject.js`

**Goal:** build an object with a **dynamic department name** as the key.

```js
export default function createEmployeesObject(departmentName, employees) {
  return { [departmentName]: employees };
}
```

**Run:** `npm run dev 11-main.js` → `{ Software: ['Bob', 'Sylvie'] }`

---

### ✅ Task 12 — Report object with method shorthand

**File:** `12-createReportObject.js`

**Goal:** return an object that contains `allEmployees` and a method `getNumberOfDepartments`.

```js
export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(allEmployees) {
      return Object.keys(allEmployees).length;
    },
  };
}
```

**Run:** `npm run dev 12-main.js` → counts departments.

---

## 🧹 ESLint & Checker Gotchas (save yourself time)

* **no-param-reassign**: don’t write to parameters (e.g., `array[i] = ...`). Create a new array/object instead.
* **no-var**: use `let` or `const`.
* **Trailing newline**: many configs require a newline at the end of each file.
* **Immutable returns** (nice‑to‑have): when possible, return copies (`{ ...obj }`, `[...arr]`) to avoid shared references.

---

## 🧩 Practice Prompts (mini‑quizzes)

1. Rewrite this to avoid parameter mutation:

```js
function incAll(nums) {
  for (let i = 0; i < nums.length; i++) nums[i] += 1;
  return nums;
}
```

2. What’s the difference between `{ departmentName: employees }` and `{ [departmentName]: employees }`?
3. Turn this into method shorthand:

```js
const x = { greet: function(name) { return `Hi ${name}`; } };
```

**Answers**

1. `return nums.map(n => n + 1);` or clone then loop.
2. The first uses the **literal** key `'departmentName'`; the second uses the **value of the variable** `departmentName`.
3. `const x = { greet(name) { return \
   `Hi \${name}`; } };`

---

## 🛠️ Debugging Flow (when a checker fails)

1. **Read the rule name** in the ESLint error (e.g., `no-param-reassign`).
2. **Minimize side effects**: prefer new arrays/objects over in‑place changes.
3. **Match the export form** exactly (e.g., `export default function ...`).
4. **Rerun just the failing main** (e.g., `npm run dev 12-main.js`).

---

## 👤 Author

**Josniel Ramos**
Software Engineering Student — Holberton School
GitHub: [https://github.com/JosnielRamos](https://github.com/JosnielRamos)
