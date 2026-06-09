# D6 — Grade Classifier + Leap Year

**Module:** 1 (Python Foundations) · **Day:** 6 · **Time budget:** 60 min (lab)

Today you'll write two small **pure functions** — they take an argument and
`return` a value (no `input()`, no `print()` inside). We test them by calling
them with `print(...)`. Both go in the same file:
`students/<your-username>/D06_grade_classifier.py`.

## Problem 1 — Grade Classifier

Write a function `classify_grade(score)` that takes a number (0–100) and
**returns** the matching letter grade as a string, using a chained
`if / elif / else`:

| Score      | Grade |
| ---------- | ----- |
| 90 or more | `"A"` |
| 80–89      | `"B"` |
| 70–79      | `"C"` |
| 60–69      | `"D"` |
| below 60   | `"F"` |

### Expected behaviour

```python
print(classify_grade(95))  # A
print(classify_grade(85))  # B
print(classify_grade(72))  # C
print(classify_grade(60))  # D
print(classify_grade(41))  # F
```

## Problem 2 — Leap Year Check

Write a function `is_leap_year(year)` that **returns** `True` or `False`.

A year is a leap year when it is **divisible by 4**, *and* (it is **not
divisible by 100** *or* it **is divisible by 400**). This single rule is a
perfect showcase for the boolean operators `and`, `or`, and `not`.

### Expected behaviour

```python
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
```

## Hints

- Order matters in a chained `if/elif/else`. Check the **highest** band first;
  the first matching branch wins and the rest are skipped.
- A value is divisible by `n` when `year % n == 0`.
- "not divisible by 100" is `year % 100 != 0` (or `not (year % 100 == 0)`).
- You can return a comparison directly: `return year % 4 == 0 and ...` — no need
  for `if ...: return True` then `else: return False`.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D06_grade_classifier.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `classify_grade()` and `is_leap_year()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Write a **triangle-type classifier**: `triangle_type(a, b, c)` takes the three
side lengths and **returns** one of `"equilateral"` (all three sides equal),
`"isosceles"` (exactly two sides equal), or `"scalene"` (all sides different).

```python
print(triangle_type(3, 3, 3))  # equilateral
print(triangle_type(5, 5, 8))  # isosceles
print(triangle_type(4, 5, 6))  # scalene
```

Hint: compare the three pairs `a == b`, `b == c`, and `a == c` and combine them
with `and` / `or`.
