# D11 — Refactor into Functions
#
# Read the full brief in problem.md.
# Build "About Me" out of small functions. The teaching point today is
# RETURN vs PRINT: the helpers RETURN values, and only main() PRINTS.


def ask_text(prompt):
    # 1. Show `prompt` to the user with input(prompt)
    # 2. RETURN whatever they typed (a string)
    pass


def ask_int(prompt):
    # 1. Ask the user with the given prompt
    # 2. Convert their answer to an int
    # 3. RETURN the integer (do not print it)
    pass


def build_bio(name, age, city, language, years):
    # Build the multi-line bio as ONE string and RETURN it.
    # Do NOT call print() in here.
    # Match the layout in problem.md (use "=" * 40 for the divider lines).
    # Tip: join lines with "\n", e.g.  line1 + "\n" + line2 + ...
    pass


def main():
    # 1. Use ask_text / ask_int to collect: name, age, city, language, years
    # 2. Call build_bio(...) and store the returned string in a variable
    # 3. print() that string
    pass


if __name__ == "__main__":
    main()
