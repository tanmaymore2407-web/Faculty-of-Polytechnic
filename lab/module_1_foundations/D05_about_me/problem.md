# D5 — About Me

**Module:** 1 (Python Foundations) · **Day:** 5 · **Time budget:** 60 min (lab)

It's Friday — time for your first **mini-project**. This week you learned
variables, types, `input()` + type conversion, and f-strings. Today you'll put
all of it into one small program that introduces *you*.

Your work goes in the file `students/<your-username>/D05_about_me.py`.

## Problem — About Me

Write a function `about_me()` that:

1. Asks the user for their **name** (a string).
2. Asks the user for their **age** (an integer).
3. Asks the user for their **city** (a string).
4. Asks the user for their **favourite programming language** (a string).
5. Asks the user for how many **years** they've been coding (an integer).
6. Prints a nicely formatted, multi-line bio block using f-strings.

Use the exact layout shown below so your output matches the expected behaviour.

### Expected behaviour

```
What is your name? Aisha
How old are you? 19
Which city are you from? Pune
Favourite programming language? Python
How many years have you been coding? 2

========================================
            ABOUT ME
========================================
Name:      Aisha
Age:       19
City:      Pune
Codes in:  Python
Coding for 2 years.
========================================
```

## Hints

- `input()` always returns a string. Convert age and years with `int(...)`.
- For whole numbers: `int(input("How old are you? "))`.
- Build the block one `print()` per line — that's the simplest way.
- To print the row of `=` signs, just put 40 of them inside a string, or use
  `"=" * 40`.
- Line up the labels by padding with spaces inside your f-string, e.g.
  `f"Name:      {name}"`.

## How to submit

1. Fork the upstream `Faculty-of-Polytechnic` repo (or click "Sync fork" if you
   already forked it) to get today's starter.
2. In your fork, create `students/<your-github-username>/D05_about_me.py`.
3. Copy the contents of `starter.py` from this folder into your new file.
4. Implement `about_me()`.
5. Commit + push to your fork, then open a PR against upstream `main`.

## ★ Stretch problem (optional)

Add **input validation** to `about_me()`:

- If the user leaves the **name** empty (just presses Enter), print
  `"Name can't be empty — try again."` and ask again.
- If the user types something that isn't a whole number for **age** (e.g.
  `"nineteen"`), print `"Please type a whole number."` and ask again.

For the age check, the clean way is `try/except ValueError` around `int(...)`.
We cover that properly on **D28**, but you're welcome to peek ahead. A simpler
beginner approach: check `age_text.isdigit()` before converting, and re-prompt
with a `while` loop if it isn't all digits.
