# D15 — Simple Calculator

**Module:** 1 (Python Foundations) · **Day:** 15 · **Time budget:** 60 min (lab)

This is the **Module 1 mini-project**. You'll bring together everything from the
functions arc (D11–D14): one small program built as a set of clean functions,
with a driver loop that ties them together.

The whole thing goes in one file: `students/<your-username>/D15_calculator.py`.

## Problem

Build a calculator that does five operations. Write **one function per
operation**, each taking two numbers and *returning* a result:

| Function          | Symbol | What it returns                          |
| ----------------- | ------ | ---------------------------------------- |
| `add(a, b)`       | `+`    | `a + b`                                  |
| `subtract(a, b)`  | `-`    | `a - b`                                  |
| `multiply(a, b)`  | `*`    | `a * b`                                  |
| `divide(a, b)`    | `/`    | `a / b` — **but guard division by zero** |
| `modulo(a, b)`    | `%`    | `a % b` — also guard a zero divisor      |

Notice that `add`, `subtract`, etc. each do exactly one job. They don't ask for
input and they don't print anything — they just take two numbers and return an
answer. That keeps them easy to test and easy to reuse.

### Guarding division by zero

Dividing by zero crashes Python. Inside `divide(a, b)` (and `modulo(a, b)`),
check **before** you divide:

```python
def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b
```

So `divide` returns *either* a number *or* a short error message. Your driver
just prints whatever comes back.

### The driver

After the five functions, write a `calculator()` function (the driver) that:

1. Asks the user for the **first number** (a `float`).
2. Asks the user for an **operator** symbol — one of `+ - * / %`.
3. Asks the user for the **second number** (a `float`).
4. Calls the matching function and prints the result like `8.0 + 2.0 = 10.0`.

Use `if / elif / else` to pick the right function for the symbol the user typed.
If the symbol isn't one of the five, print `Unknown operator: <symbol>`.

### Expected behaviour

```
First number: 8
Operator (+ - * / %): /
Second number: 2
8.0 / 2.0 = 4.0
```

A divide-by-zero session:

```
First number: 7
Operator (+ - * / %): /
Second number: 0
7.0 / 0.0 = Error: cannot divide by zero
```

## Hints

- `input()` always returns a string. Wrap the two numbers in `float(...)`.
- Don't convert the operator — `+ - * / %` are just text you compare with `==`.
- Each operation function is one or two lines. Keep them tiny.
- The driver decides *which* function to call; the functions do the math. Don't
  mix the two jobs.
- Build the chooser as a chain: `if op == "+": result = add(a, b)` …
  `elif op == "/": result = divide(a, b)` … `else: print("Unknown operator: ...")`.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D15_calculator.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement the five operation functions and the `calculator()` driver.
5. Run it and check it against the sessions above.
6. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Keep a **history** of every calculation. Lists were covered on Day 3, so you
have all the tools.

1. Before the loop, create an empty list: `history = []`.
2. Turn the driver into a loop so the user can do several calculations in a row.
   After each one, append a record string to `history`, e.g. `"3.0 + 4.0 = 7.0"`.
3. Add a special operator the user can type to control the program:
   - `history` — print every record stored so far, one per line.
   - `q` — quit the loop.

Example session:

```
Operator (+ - * / % | history | q): +
First number: 3
Second number: 4
3.0 + 4.0 = 7.0
Operator (+ - * / % | history | q): history
3.0 + 4.0 = 7.0
Operator (+ - * / % | history | q): q
Bye!
```
