# D7 — Sum 1..N + Times Tables

**Module:** 1 (Python Foundations) · **Day:** 7 · **Time budget:** 60 min (lab)

Today you'll write two small programs that use `for` loops and `range()`. Both
go in the same file: `students/<your-username>/D07_loops_and_tables.py`.

## Problem 1 — Sum 1 to N

Write a function `sum_to_n(n)` that returns the sum `1 + 2 + 3 + ... + n` using
a **`for` loop and an accumulator** (a running total). Do **not** use the
`n * (n + 1) / 2` formula — the whole point is to practise the loop.

1. Start with a running total of `0`.
2. Loop over the numbers `1` through `n` using `range`.
3. Add each number to the running total.
4. `return` the total at the end.

### Expected behaviour

```python
print(sum_to_n(5))   # 15
print(sum_to_n(1))   # 1
print(sum_to_n(10))  # 55
```

## Problem 2 — Times Table

Write a function `times_table(n)` that **prints** the multiplication table for
`n`, from `1` up to `10`. It does not return anything — it just prints 10 lines.

Each line has the form `n x i = n*i`.

### Expected behaviour

```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

## Hints

- `range(1, n + 1)` gives you `1, 2, 3, ..., n` — remember `range` **stops one
  short** of the second number.
- The accumulator pattern: create `total = 0` **before** the loop, then do
  `total = total + i` (or `total += i`) **inside** the loop.
- In `times_table`, build each line with an f-string: `f"{n} x {i} = {n * i}"`.
- Problem 1 **returns** a value; Problem 2 **prints** lines. Don't mix them up.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D07_loops_and_tables.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `sum_to_n(n)` and `times_table(n)`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Write a function `factorial(n)` that returns `n!` — the product
`1 * 2 * 3 * ... * n` — using a `for` loop and an accumulator. This is just like
`sum_to_n`, but you **multiply** instead of add, so your running total must
**start at `1`**, not `0` (anything times `0` is `0`!).

```python
print(factorial(5))  # 120
print(factorial(1))  # 1
```
