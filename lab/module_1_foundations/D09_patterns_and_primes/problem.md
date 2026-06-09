# D9 — Patterns + Prime Check

**Module:** 1 (Python Foundations) · **Day:** 9 · **Time budget:** 60 min (lab)

Today is a *combine* day. You're not learning new syntax — you're putting loops
and conditions together. Both functions go in the same file:
`students/<your-username>/D09_patterns_and_primes.py`.

## Problem 1 — Triangle pattern

Write a function `print_triangle(height)` that prints a left-aligned right
triangle of `*` characters. Row 1 has one star, row 2 has two stars, and so on,
down to row `height`, which has `height` stars.

This is a classic *nested loop*: an outer loop for the rows, and inside it a way
to build the right number of stars for that row.

### Expected behaviour

```
print_triangle(5)
*
**
***
****
*****
```

## Problem 2 — Prime check

Write a function `is_prime(n)` that returns `True` if `n` is a prime number and
`False` otherwise.

A prime number is a whole number greater than 1 whose only divisors are 1 and
itself. So:

- `is_prime(7)` → `True`
- `is_prime(10)` → `False` (because 2 divides it)
- `is_prime(1)` → `False`
- `is_prime(0)` and any negative number → `False`

Use a loop to test the possible divisors. This is the **flag / early-decision**
pattern: assume the number is prime, then loop looking for a divisor — the
moment you find one, you can decide and stop.

### Expected behaviour

```
print(is_prime(7))    # True
print(is_prime(10))   # False
print(is_prime(1))    # False
print(is_prime(2))    # True
```

## Hints

- For Problem 1, an inner `for` loop that prints a star with `print("*", end="")`
  works, or you can build the row as a string first. Don't forget the newline at
  the end of each row.
- For Problem 2, handle `n < 2` first and return `False` straight away.
- To test divisibility, use the remainder operator: `n % d == 0` means `d`
  divides `n` evenly.
- You only need to test divisors from `2` up to `n - 1`. As soon as one divides
  `n`, you know it's not prime — `return False` immediately.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D09_patterns_and_primes.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `print_triangle()` and `is_prime()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Write a function `primes_up_to(limit)` that prints every prime number from `2`
up to and including `limit`, one per line. Reuse your `is_prime()` function
inside a loop — don't rewrite the prime-checking logic.

### Expected behaviour

```
primes_up_to(10)
2
3
5
7
```
