# ES6 Classes

> A friendly, visual guide to modern OOP in JavaScript using the **ES6\_classes** tasks. Learn how to model real domains with classes, validate state, use inheritance safely, and leverage powerful ES features like symbols and coercion hooks.

---

## 🎯 Goals

* Understand **class syntax**: constructors, fields, methods, static members.
* Apply **encapsulation** with getters/setters + validation.
* Use **inheritance** responsibly (`extends`, `super`) and emulate **abstract** contracts.
* Control **string/number coercion** with `Symbol.toPrimitive` and `Symbol.toStringTag`.
* Build **polymorphic cloning** with `Symbol.species`.
* Avoid hoisting pitfalls (TDZ) and follow checker-friendly patterns.

---

## 🚀 Quick Start

```bash
# From the repository root
cd ES6_classes
npm run dev 6-main.js   # run a specific task's demo
```

> Tip: Each task has an implementation file (e.g., `6-sky_high.js`) and a small `*-main.js` runner.

---

## 🧱 Core Concepts (Cheat‑Sheet)

### Class Basics

```js
class Person {
  constructor(name) { this._name = name; } // underscore-backed field
  get name() { return this._name; }
  set name(v) { if (typeof v !== 'string') throw new TypeError('name'); this._name = v; }
  greet() { return `Hi, ${this._name}`; } // instance method (on prototype)
  static from(obj) { return new Person(obj.name); } // static factory
}
```

* **Constructor** initializes instance state.
* **Getters/Setters** enforce validation at creation *and* updates.
* **Instance methods** live on `Class.prototype` (memory‑efficient).
* **Static methods** belong to the class itself (utilities/factories).

### Inheritance & Abstract Contracts

```js
class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') throw new TypeError('sqft');
    if (new.target !== Building && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage)
      throw new Error('Class extending Building must override evacuationWarningMessage');
    this._sqft = sqft;
  }
  get sqft() { return this._sqft; }
  evacuationWarningMessage() { throw new Error('Class extending Building must override evacuationWarningMessage'); }
}

class SkyHighBuilding extends Building {
  constructor(sqft, floors) { super(sqft); this._floors = floors; }
  get floors() { return this._floors; }
  evacuationWarningMessage() { return `Evacuate slowly the ${this.floors} floors`; }
}
```

* Use a **base class** to enforce a contract; subclasses must **override** required methods.
* Call `super(...)` before using `this` in subclass constructors.

### Controlling String & Number Coercion

```js
class HolbertonClass {
  constructor(size, location) { this._size = size; this._location = location; }
  [Symbol.toPrimitive](hint) { return hint === 'number' ? this._size : this._location; }
}
```

* `Number(obj)` → uses `hint: 'number'` → returns size.
* `String(obj)` / template literal → uses `'string'|'default'` → returns location.

### Customizing Default String Description

```js
class Airport {
  constructor(name, code) { this._name = name; this._code = code; }
  get [Symbol.toStringTag]() { return this._code; } // → "[object SFO]"
}
```

* Great for logs/inspectors: concise identity instead of `[object Object]`.

### Polymorphic Cloning with `Symbol.species`

```js
class Car {
  constructor(brand, motor, color) { this._brand = brand; this._motor = motor; this._color = color; }
  cloneCar() { const Ctor = this.constructor[Symbol.species] || this.constructor; return new Ctor(); }
  static get [Symbol.species]() { return this; } // subclasses inherit: clones keep concrete type
}
class TestCar extends Car {}
```

* Subclasses can override species:

```js
class EVCar extends Car { static get [Symbol.species]() { return Car; } }
```

### Hoisting & TDZ (Temporal Dead Zone)

* **Function declarations** are callable before their line (fully hoisted).
* **class / let / const** are hoisted but **uninitialized** until their line → accessing early throws **ReferenceError**.
* **Rule of thumb**: define classes before use; enable ESLint `no-use-before-define`.

---

## 🧩 Task Highlights (with real‑world context)

### 0) ClassRoom — Minimal Encapsulation

* Define a class with one field `_maxStudentsSize`.
* **Why it matters:** models capacity constraints (e.g., scheduling systems). A getter later enables derived logic like `isFull()`.

### 1) initializeRooms — Factories

* Build an array of instances from config values `[19, 20, 34]`.
* **Why it matters:** seed data, fixtures, or runtime configuration → map to domain objects.

### 2) HolbertonCourse — Validated State

* Getters/setters verify types: string/number/array of strings; throw early.
* **Why it matters:** prevent invalid domain states; centralize checks.

### 3) Currency — Plain Domain Value Object

* `_code`, `_name`; method `displayFullCurrency()` → `"Dollars ($)"`.
* **Why it matters:** clean formatting/presentation from a single source of truth.

### 4) Pricing — Instance vs Static

* Instance: `displayFullPrice()` (uses embedded `Currency`).
* Static: `convertPrice(amount, rate)` (utility, no instance needed).
* **Why it matters:** split responsibilities; test utilities in isolation.

### 5) Building — Abstract Contract

* Base class enforces `evacuationWarningMessage()`.
* **Why it matters:** downstream systems can call the same API on every building type.

### 6) SkyHighBuilding — Safe Override

* Adds `_floors` and overrides evacuation message.
* **Why it matters:** specialize behavior without changing callers.

### 7) Airport — String Identity

* `Symbol.toStringTag` → `"[object SFO]"`.
* **Why it matters:** tidy logs, easier observability.

### 8) HolbertonClass — Coercion Hooks

* `Symbol.toPrimitive` to control `Number(obj)` and `String(obj)`.
* **Why it matters:** ergonomic display vs. numeric logic (capacity, IDs).

### 9) Hoisting — Define Before Use

* Fix TDZ errors by declaring classes before instantiation; correct getters.
* **Why it matters:** predictable load order, fewer runtime surprises.

### 10) Car — Polymorphic Clone

* `cloneCar()` chooses constructor via `Symbol.species`.
* **Why it matters:** cloning keeps concrete subtype automatically (framework-friendly). Subclasses can opt out by overriding species.

---

## 🛠️ Patterns You’ll Actually Use

* **Factories**: `static from(dto)` to construct from API payloads.
* **Value Objects**: immutable currency/price/date wrappers with formatting + math.
* **Strategy via Composition**: rather than many subclasses, inject behaviors (e.g., `new Building(sqft, new StairwellEvacuation())`).
* **Adapters**: classes that wrap third‑party SDKs with a stable project API.

---

## ✅ Lint & Checker Tips

* Use **default exports** exactly as required by each task.
* Keep **trailing newlines** and avoid mutating parameters (`no-param-reassign`).
* Remember TDZ: define classes before use (`no-use-before-define`).
* Prefer getters/setters for validation; call setters inside constructors.

---

## 🧪 Mini‑Quizzes

1. Why is `Symbol.toPrimitive` preferred over `valueOf()/toString()` for controlling coercion?
2. When should a method be `static` vs. instance?
3. What does overriding `static get [Symbol.species]()` change for cloning?

**Answers**

1. It’s the first consulted hook with explicit `hint` (number/string/default); most predictable.
2. Make it `static` when it doesn’t depend on instance state (pure utility/factory).
3. It selects which **constructor** is used to create derived objects, enabling clones to be a base or the same subtype.

---

## 📚 Further Reading

* MDN: Classes, Inheritance, Getters/Setters
* MDN: Symbols (`toPrimitive`, `toStringTag`, `species`)
* ESLint: `no-use-before-define`, `no-param-reassign`

---

## 👤 Author

**Josniel Ramos** — Software Engineering Student, Holberton School
