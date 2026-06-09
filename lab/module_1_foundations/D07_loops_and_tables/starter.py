# D7 — Sum 1..N + Times Tables
#
# Read the full brief in problem.md.
# Implement both functions below. Run the file to test.

def sum_to_n(n):
    # 1. Make a running total, starting at 0
    # 2. Loop over the numbers 1 through n with range(1, n + 1)
    # 3. Add each number to the running total
    # 4. Return the total (use a for loop + accumulator, NOT a formula)
    pass


def times_table(n):
    # 1. Loop over i from 1 through 10 with range(1, 11)
    # 2. Print each line in the form: f"{n} x {i} = {n * i}"
    #    (this function PRINTS — it does not return anything)
    pass


if __name__ == "__main__":
    print(sum_to_n(5))  # expected: 15
    print()  # blank line between the two problems
    times_table(7)
