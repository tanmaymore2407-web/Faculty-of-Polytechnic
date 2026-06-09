# D13 — Scope Bug-Hunt: the broken shopping cart

**Module:** 1 (Python Foundations) · **Day:** 13 · **Time budget:** 60 min (lab)

Today is a **bug-hunt**. You are *not* filling in blanks — you are given a
short program that already runs, but prints the **wrong total**. The reason is
**scope**: the functions lean on a shared *global* variable called `total`
instead of taking their inputs as **parameters** and handing back results with
**return**.

Copy `starter.py` into `students/<your-username>/D13_scope_bughunt.py`, run it,
watch it lie to you, then **refactor** until it prints the correct numbers.

## Your task

1. Run the starter. It prints a cart total of `15` and tax of `15.75`.
   Those are **wrong** — three items priced 40, 25 and 15 should total **80**.
2. Find the two buggy spots (each is marked with a `# BUG:` comment).
3. Refactor so that:
   - `add_item` takes the **running total** and a **price** as parameters and
     **returns** the new running total. It must not read or overwrite the
     global `total`, and must not use the `global` keyword.
   - `apply_tax` takes the **cart total** as a parameter and **returns** the
     total with 5% tax added. It must not read the global `total`.
   - `main` keeps its own local `total` (starting at `0`), updates it from
     what `add_item` **returns**, and passes that into `apply_tax`.
4. The rule to follow everywhere: **pass it in, return it out.** No function
   should depend on a global variable.

### Expected behaviour

After your fix, running the file should print exactly:

```
Items added. Cart total: 80
With 5% tax: 84.00
```

## Hints

- A variable created **inside** a function is *local* — it disappears when the
  function ends. That is a good thing. Use it.
- `add_item(running_total, price)` should `return running_total + price`. In
  `main`, capture it: `total = add_item(total, 40)`.
- If you ever feel the urge to type `global`, that is the signal to **pass the
  value in as a parameter** instead.
- Format money to 2 decimals with `f"{value:.2f}"`.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D13_scope_bughunt.py`.
3. Copy `starter.py` from this folder into your new file.
4. Fix the two scope bugs so the output matches **Expected behaviour**.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

There is a second, sneakier scope bug hiding for you to add and then fix.
Extend the program with a `count_items` helper:

```python
def count_items(prices):
    for n in prices:          # `n` is a loop variable — it is LOCAL to this loop
        ...
    return ...                # return how many items are in `prices`
```

Now, in `main`, **after** the loop runs, try to `print(n)`. In some other
languages that loop variable would have leaked out and still be usable — and
beginners often *assume* a value survives where it shouldn't. Write a one-line
comment explaining what actually happens in Python when you read a name that
was only ever assigned inside another function's scope, and make sure your
final program does **not** rely on any name leaking out of a loop or function.
