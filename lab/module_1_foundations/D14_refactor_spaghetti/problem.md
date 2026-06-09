# D14 — Refactor: Spaghetti → Clean

**Module:** 1 (Python Foundations) · **Day:** 14 · **Time budget:** 60 min (lab)

Today is different. You are **not** writing new behaviour. The `starter.py` in
this folder is a **working** program — run it and it prints a clean report card
for three students. The catch: the code is *spaghetti*. One long flat block,
the same calculation copy-pasted three times, magic numbers, and one-letter
names like `n`, `a`, `t`, `av`.

Your job is to **refactor** it: turn it into clean, named functions **without
changing a single character of its output.** Refactoring means improving the
*shape* of the code while keeping its *behaviour* identical.

## The task

Work inside `students/<your-username>/D14_refactor_spaghetti.py` (a copy of
`starter.py`).

1. **Capture the truth first.** Run the starter and save its exact output (or
   just keep `example_run.txt` open). This is your target — it must not change.
2. **Extract a function.** The three student blocks are nearly identical. Write
   one function, e.g. `print_report(name, m1, m2, m3)`, that prints the report
   for one student.
3. **Replace repetition with calls.** Delete the three copy-pasted blocks and
   call your function three times instead.
4. **Name the magic numbers.** Give names to the constants `3` (number of
   subjects), `35` (pass mark) and `75` (distinction mark) so the code reads
   like English.
5. **Use clear names.** No more `n`, `a`, `b`, `c`, `t`, `av`.
6. **Run it again.** The output must be **byte-for-byte identical** to step 1.

Follow the `# TODO:` comments in `starter.py` — each one marks a smell to fix.

### Expected behaviour

The output **before and after** your refactor must be exactly this:

```
===== REPORT CARD =====
Name: Aarav
Marks: 40, 55, 70
Total: 165 / 300
Average: 55.0
Result: PASS
-----------------------
Name: Diya
Marks: 30, 28, 33
Total: 91 / 300
Average: 30.33
Result: FAIL
-----------------------
Name: Kabir
Marks: 88, 91, 79
Total: 258 / 300
Average: 86.0
Result: PASS (Distinction)
-----------------------
```

## Hints

- **Refactor in tiny steps.** Change one thing, run the program, check the
  output still matches, then change the next thing. Don't rewrite everything at
  once.
- The repeated block is your function *body*. The bits that change between
  students (the name and the three marks) are your function *parameters*.
- Keep the exact strings. `"Average: "` then `str(round(av, 2))` produces
  `55.0`, not `55.00`. Don't "tidy" the formatting — that would change the
  output, which is not allowed today.
- A magic number becomes a named constant like `PASS_MARK = 35` written once,
  near the top, then used by name everywhere.
- Watch the result rule: `FAIL` if average `< 35`, `PASS (Distinction)` if
  average `>= 75`, otherwise `PASS`. Keep the order of the checks the same.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D14_refactor_spaghetti.py`.
3. Copy `starter.py` from this folder into your new file.
4. Refactor it into clean functions, keeping the output identical.
5. Open a Pull Request against the upstream `main` branch.

## ★ Stretch problem (optional)

Once `print_report(name, m1, m2, m3)` exists, get rid of the three separate
calls too. Put each student's data in a small structure and **loop** over it:

```python
students = [
    ("Aarav", 40, 55, 70),
    ("Diya",  30, 28, 33),
    ("Kabir", 88, 91, 79),
]
for name, m1, m2, m3 in students:
    print_report(name, m1, m2, m3)
```

Now adding a fourth student is **one new line** in the list — no copy-pasting,
no new `print` calls. The output must still match exactly (with the fourth
student's report appended). That one-line-to-extend property is the whole point
of refactoring well.
