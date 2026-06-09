# D10 — Number Guessing Game

**Module:** 1 (Python Foundations) · **Day:** 10 · **Time budget:** 60 min (lab)

This is your first **mini-project**: a small program with a real game loop. The
computer is "thinking of" a secret number, and the player keeps guessing until
they get it. You'll build the loop that powers almost every game ever written:
ask, check, give feedback, repeat.

Your file goes in `students/<your-username>/D10_guessing_game.py`.

## The secret number

Normally the computer would *randomly* pick the secret number, but you haven't
learned `random` yet — that's **Day 29**. So for today we **hard-code** it at
the very top of the file:

```python
SECRET = 42
# On Day 29 you'll learn `random` to make the computer pick this for you.
```

That's fine: the point today is the *loop and the feedback logic*, not the
randomness.

## Problem — `play_game()`

Write a function `play_game()` that:

1. Keeps a counter of how many guesses the player has made (start it at `0`).
2. Loops forever (`while True:`), and on each pass:
   - Asks the player for a guess and converts it to an `int`.
   - Adds `1` to the guess counter.
   - If the guess is **greater** than `SECRET`, prints `Too high!`.
   - If the guess is **less** than `SECRET`, prints `Too low!`.
   - If the guess is **correct**, prints
     `Correct! You got it in <n> tries.` and **stops the loop** with `break`.

Use `if` / `elif` / `else` for the three cases, and `break` to leave the loop
once the player wins.

### Expected behaviour

```
Guess the number (1-100): 50
Too high!
Guess the number (1-100): 25
Too low!
Guess the number (1-100): 37
Too low!
Guess the number (1-100): 42
Correct! You got it in 4 tries.
```

(The number of tries in the final line is your guess counter.)

## Hints

- `input()` always returns a string — wrap it in `int(...)` to compare numbers.
- The counter pattern: start with `tries = 0` *before* the loop, then write
  `tries = tries + 1` (or `tries += 1`) at the top of each pass.
- `while True:` loops forever; the only way out is `break`. Put your `break`
  in the branch that runs when the guess is correct.
- Build the winning message with an f-string: `f"Correct! You got it in {tries} tries."`

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D10_guessing_game.py`.
3. Copy `starter.py` from this folder into your new file (keep the `SECRET = 42`
   line at the top).
4. Implement `play_game()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Add a **warmer / colder** hint. After the first guess, compare how far *this*
guess is from `SECRET` to how far the *previous* guess was:

- If this guess is **closer** to `SECRET` than the last one, also print `Warmer`.
- If it's **further** away, print `Colder`.

To measure "how far away" a guess is, use the distance `abs(guess - SECRET)`
(`abs()` gives the size of a number, ignoring its sign — `abs(-8)` is `8`). You'll
need to remember the previous guess in a variable so you can compare against it
on the next pass. There's nothing to print on the *very first* guess, since
there's no previous guess to compare to yet.
