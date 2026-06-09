# D9 — Patterns + Prime Check
#
# Read the full brief in problem.md.
# Implement both functions below. Run the file to test.


def print_triangle(height):
    # 1. Loop over the rows from 1 up to and including `height`
    # 2. For each row i, print i stars (a "*" character) on one line
    # 3. Tip: an inner loop with print("*", end="") plus a final print()
    #    will give you one row, or build the row as a string first
    pass


def is_prime(n):
    # 1. If n is less than 2, it cannot be prime -> return False
    # 2. Loop over possible divisors d from 2 up to n - 1
    # 3. If n % d == 0, then d divides n -> return False immediately
    # 4. If the loop finishes without finding a divisor -> return True
    pass


if __name__ == "__main__":
    print_triangle(5)
    print()  # blank line between the two problems
    print(is_prime(7))
    print(is_prime(10))
    print(is_prime(1))
