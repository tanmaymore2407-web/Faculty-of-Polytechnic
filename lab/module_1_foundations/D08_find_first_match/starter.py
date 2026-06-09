# D8 — Find First Match
#
# Read the full brief in problem.md.
# Implement both functions below. Run the file to test.

def countdown(n):
    # 1. Make a variable that starts at n
    # 2. while it is still >= 1: print it, then subtract 1
    #    (forgetting to subtract 1 = infinite loop!)
    # 3. After the loop, print "Liftoff!"
    pass


def first_multiple(n, start):
    # 1. Make a candidate variable that starts at `start`
    # 2. Loop: if candidate % n == 0, you found it -> break
    # 3. Otherwise move to the next candidate (add 1)
    # 4. Return the candidate you found
    pass


if __name__ == "__main__":
    countdown(5)
    print()  # blank line between the two problems
    print(first_multiple(7, 50))  # 56
