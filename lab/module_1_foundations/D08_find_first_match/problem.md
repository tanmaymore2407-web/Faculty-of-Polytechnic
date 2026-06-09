# D8 — Find First Match

**Module:** 1 (Python Foundations) · **Day:** 8 · **Time budget:** 60 min (lab)

Today is all about the `while` loop — the loop you reach for when you don't know
in advance how many times you need to repeat. Both functions go in the same
file: `students/<your-username>/D08_find_first_match.py`.

## Problem 1 — Countdown

Write a function `countdown(n)` that uses a **`while` loop** to count down from
`n` to `1`, printing one number per line, then prints `Liftoff!`.

- Assume `n` is a positive integer.
- You must use a `while` loop (not a `for` loop) — practise updating the loop
  variable yourself.

### Expected behaviour

```
countdown(5)

5
4
3
2
1
Liftoff!
```

## Problem 2 — First Multiple

Write a function `first_multiple(n, start)` that **returns** the first integer
that is greater than or equal to `start` and is divisible by `n`. Find it with a
`while` loop and `break` — the classic "find-first-match" pattern.

1. Begin checking at `start`.
2. Walk upward one number at a time.
3. As soon as you find a number divisible by `n`, `break` out and return it.

### Expected behaviour

```python
print(first_multiple(7, 50))   # 56
print(first_multiple(10, 10))  # 10
print(first_multiple(3, 1))    # 3
```

## Hints

- A `while` loop has a **condition** that is checked before every pass. The loop
  keeps going while the condition is `True`.
- For `countdown`, start with a variable at `n` and **subtract 1 each pass** —
  if you forget to subtract, the loop never ends (an *infinite loop*).
- "Divisible by `n`" means `number % n == 0`.
- The find-first pattern: `while True:` … check … `if match: break`. Don't forget
  to move to the next candidate inside the loop, or you'll loop forever on the
  same number.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D08_find_first_match.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `countdown()` and `first_multiple()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Write a function `collatz_steps(n)` that returns how many steps it takes to
reach `1` from `n` using the Collatz rule, found with a `while` loop:

- If the current number is **even**, divide it by 2 (`n // 2`).
- If it is **odd**, replace it with `3 * n + 1`.
- Count one step for each replacement. Stop when you reach `1`.

### Expected behaviour

```python
print(collatz_steps(1))   # 0  (already at 1)
print(collatz_steps(6))   # 8
print(collatz_steps(27))  # 111
```
