# D12 — Geometry Helpers

**Module:** 1 (Python Foundations) · **Day:** 12 · **Time budget:** 60 min (lab)

Today you'll write small functions that take **multiple parameters**, use a
**default parameter value**, and return **multiple values as a tuple**. Both go
in the same file: `students/<your-username>/D12_geometry_helpers.py`.

These are pure functions — they don't ask for input. You test them by calling
them and printing the results.

## Problem 1 — Rectangle

Write a function `rectangle(width, height)` that returns a tuple
`(area, perimeter)`, where:

- `area = width * height`
- `perimeter = 2 * (width + height)`

Return both values as a single tuple: `return area, perimeter`.

### Expected behaviour

```
a, p = rectangle(3, 4)
print(a)   # 12
print(p)   # 14

a, p = rectangle(10, 2)
print(a)   # 20
print(p)   # 24
```

Notice how the caller **unpacks** the returned tuple into two names with
`a, p = rectangle(3, 4)`.

## Problem 2 — Circle

Write a function `circle(radius, pi=3.14159)` that returns a tuple
`(area, circumference)`, where:

- `area = pi * radius * radius`
- `circumference = 2 * pi * radius`

The `pi` parameter has a **default value** of `3.14159`, so the caller can leave
it out. If they pass a different value, it overrides the default.

### Expected behaviour

```
a, c = circle(2)
print(round(a, 2))   # 12.57   (uses the default pi = 3.14159)
print(round(c, 2))   # 12.57

a, c = circle(2, pi=3.14)
print(round(a, 2))   # 12.56   (caller's pi = 3.14 overrides the default)
print(round(c, 2))   # 12.56
```

## Hints

- To return two values: `return area, perimeter`. Python packs them into a
  tuple for you.
- To receive two values: `a, p = rectangle(3, 4)`. This is called **unpacking**.
- A default value goes in the `def` line: `def circle(radius, pi=3.14159):`.
- Do **not** import `math`. Use the constant `3.14159` (or whatever the caller
  passes) for pi.
- `round(value, 2)` rounds a number to 2 decimal places — handy for printing.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D12_geometry_helpers.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `rectangle()` and `circle()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Write a function `box(length, width, height=1)` that returns a tuple
`(volume, surface_area)`, where:

- `volume = length * width * height`
- `surface_area = 2 * (length*width + length*height + width*height)`

The `height` parameter defaults to `1`. Show that `box(2, 3)` (a flat sheet,
height 1) and `box(2, 3, 4)` give different results, and unpack the result with
`v, s = box(2, 3, 4)`.
