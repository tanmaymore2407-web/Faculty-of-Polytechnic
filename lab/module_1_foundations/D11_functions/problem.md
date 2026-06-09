# D11 — Refactor into Functions

**Module:** 1 (Python Foundations) · **Day:** 11 · **Time budget:** 60 min (lab)

On Day 5 you wrote one big `about_me()` function that did *everything*: it asked
all the questions, built the bio text, and printed it — all tangled together.
Today you'll learn the most important refactor in programming: **split one big
job into small, named functions**, each doing exactly one thing.

The big idea today is **return vs print**. A function that *returns* a value
hands it back to whoever called it, so it can be reused. A function that only
*prints* throws the value away on the screen. Most of your helpers today will
**return** — and only `main()` will print.

Your work goes in the file `students/<your-username>/D11_functions.py`.

## Problem — Refactor "About Me" into functions

Take the same "About Me" idea from D5, but build it out of **four small
functions** instead of one big one:

1. `ask_text(prompt)` — takes a prompt string, asks the user with `input()`,
   and **returns** the text they typed.
2. `ask_int(prompt)` — takes a prompt string, asks the user, converts the answer
   to an `int`, and **returns** the integer.
3. `build_bio(name, age, city, language, years)` — takes the five facts as
   **parameters** and **returns** the finished, multi-line bio string.
   It must **not** call `print()`.
4. `main()` — wires everything together: it calls `ask_text` / `ask_int` to
   collect the five facts, calls `build_bio(...)` to get the bio string, and
   then **prints** that string.

The labels and layout are the same as D5, so your output matches the expected
behaviour below.

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

- A function **returns** a value with the `return` keyword:
  `def ask_text(prompt): return input(prompt)`.
- `ask_int` is just `ask_text` with an `int(...)` around it — but write it as its
  own function so the conversion lives in one place.
- `build_bio` should build the whole block as **one string** and `return` it.
  Join lines with `\n` (the newline character), or build it piece by piece with
  `+`. The `=` divider is `"=" * 40`.
- `build_bio` does **not** ask anything and does **not** print anything — it only
  takes its five parameters and returns text. You can test it on its own:
  `print(build_bio("Sam", 20, "Pune", "Python", 1))`.
- In `main()`, store the result: `bio = build_bio(...)` then `print(bio)`.
- Remember: a function must be **defined above** where you call it (or at least
  before `main()` runs).

## How to submit

1. Fork the upstream `Faculty-of-Polytechnic` repo (or click "Sync fork" if you
   already forked it) to get today's starter.
2. In your fork, create `students/<your-github-username>/D11_functions.py`.
3. Copy the contents of `starter.py` from this folder into your new file.
4. Implement `ask_text`, `ask_int`, `build_bio`, and `main`.
5. Commit + push to your fork, then open a PR against upstream `main`.

## ★ Stretch problem (optional)

Add a helper `greeting(name)` that **returns** a friendly, time-independent
greeting line and put it at the top of the bio. It must `return` a string (not
print it), for example:

```
Hey Aisha, nice to meet you!

========================================
            ABOUT ME
========================================
...
```

Write `greeting(name)` as its own function that returns the line, call it inside
`build_bio` (or in `main` and pass the result in), and add the greeting plus a
blank line above the `====` divider. Keep it beginner-simple — one `return`
with an f-string is enough.
