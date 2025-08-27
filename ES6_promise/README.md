# ES6 Promises

> A clean, visual guide to Promises for the **ES6\_promise** project. Learn how to create, compose, and handle async flows with confidence.

---

## 🎯 Goals

* Understand **what Promises are** and why they help.
* Build and consume Promises with **then / catch / finally**.
* Run work **in parallel** (all, allSettled, race, any).
* Use **async/await** without losing correctness (serial vs parallel).
* Apply the patterns to each task in **ES6\_promise**.

---

## ⚙️ Quick Start

```bash
# from the project root
cd ES6_promise
npm install
npm run dev 0-main.js      # run an example
npm test 6-final-user.test.js
npm run lint
```

---

## 🧠 Promises in One Picture

**pending** → (resolve) → **fulfilled(value)**
**pending** → (reject)  → **rejected(reason)**

Handlers run on the **microtask queue** (after current call stack).

---

## 🧱 Core Syntax

### Create / Settle

```js
// Already-settled helpers
Promise.resolve(value)
Promise.reject(new Error('reason'))

// Start brand-new async work
new Promise((resolve, reject) => {
  // ... do work ...
  // resolve(result) or reject(error)
});

// Async function sugar
async function f() {
  return value;  // -> fulfilled
  // throw new Error('x'); -> rejected
}
```

### Consume / Chain

```js
promise
  .then(value => next)       // success path (return to pass value on)
  .catch(err => recovery)    // handle rejection (return to continue)
  .finally(() => cleanup);   // always runs; doesn’t change outcome
```

### Parallel Composition

```js
await Promise.all([p1, p2]);        // all succeed or reject fast
await Promise.allSettled([p1, p2]); // always resolves w/ statuses
await Promise.race([p1, p2]);       // first to settle wins
await Promise.any([p1, p2]);        // first to fulfill wins
```

### Async/Await Patterns

```js
// Sequential (A then B)
const a = await A();
const b = await B(a);

// Parallel (A and B at the same time)
const pA = A();
const pB = B();
const [a, b] = await Promise.all([pA, pB]);
```

---

## ✅ Task-by-Task Cheat Sheet

### 0) **getResponseFromAPI** — return a Promise

```js
export default function getResponseFromAPI() {
  return Promise.resolve();
}
```

### 1) **getFullResponseFromAPI(success)** — resolve/reject by boolean

```js
return success
  ? Promise.resolve({ status: 200, body: 'Success' })
  : Promise.reject(new Error('The fake API is not working currently'));
```

### 2) **handleResponseFromAPI(promise)** — chain handlers

```js
return promise
  .then(() => ({ status: 200, body: 'success' }))
  .catch(() => new Error())
  .finally(() => console.log('Got a response from the API'));
```

### 3) **handleProfileSignup** — parallel success or offline

```js
return Promise.all([uploadPhoto(), createUser()])
  .then(([photo, user]) => {
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  })
  .catch(() => console.log('Signup system offline'));
```

### 4) **signUpUser** — fulfilled data

```js
return Promise.resolve({ firstName, lastName });
```

### 5) **uploadPhoto(fileName)** — rejected with message

```js
return Promise.reject(new Error(`${fileName} cannot be processed`));
```

### 6) **handleProfileSignup(first, last, file)** — allSettled + map

```js
return Promise.allSettled([
  signUpUser(first, last),
  uploadPhoto(file),
]).then(results => results.map(r => ({
  status: r.status,
  value: r.status === 'fulfilled' ? r.value : String(r.reason),
})));
```

### 7) **loadBalancer(chinaDownload, USDownload)** — race

```js
return Promise.race([chinaDownload, USDownload]);
```

### 8) **divideFunction(numerator, denominator)** — throw on 0

```js
if (denominator === 0) throw new Error('cannot divide by 0');
return numerator / denominator;
```

### 9) **guardrail(mathFunction)** — try/catch/finally queue

```js
const queue = [];
try { queue.push(mathFunction()); }
catch (e) { queue.push(String(e)); }
finally { queue.push('Guardrail was processed'); }
return queue;
```

---

## 🧩 Patterns You’ll Reuse

* **Return** inside `.then` / `.catch` to pass values along.
* Use `Promise.allSettled` when you need **all outcomes**.
* Use `Promise.race` for **first settled**, `Promise.any` for **first fulfilled**.
* Turn errors into strings for logs/tests: `String(err)` gives `"Error: ..."`.
* Keep error text **exact** for checkers.

---

## 🪤 Common Pitfalls (and Fixes)

* **Anti-pattern**: `new Promise(resolve => resolve(x))` → use `Promise.resolve(x)`.
* **Silent failure**: forgetting `.catch` or `try/catch` around `await`.
* **Accidental serialization**: `await A(); await B();` when A and B are independent → start both first, then `await Promise.all`.
* **Wrong mapping**: `allSettled` rejected entries use `reason`, not `value`.
* **Exact messages**: e.g., `'cannot divide by 0'` (case/spaces matter).

---

## 🧪 Debugging Tips

* Log shapes to learn contracts: `.then(console.log)`.
* Add a **final** `.catch(console.error)` while developing.
* Use small **delay** helpers to simulate timing:

```js
const delay = ms => new Promise(res => setTimeout(res, ms));
```

---

## 📚 Quick Reference

```js
p.then(onFulfilled).catch(onRejected).finally(onAlways);
Promise.all(iterable)        // all succeed → array; any fail → reject
Promise.allSettled(iterable) // statuses for each (never throws)
Promise.race(iterable)       // first settled wins (resolve or reject)
Promise.any(iterable)        // first fulfilled wins (AggregateError if all reject)
```

---

## ✍️ Author

**Josniel Ramos** — Holberton School
GitHub: [https://github.com/JosnielRamos](https://github.com/JosnielRamos)

---
