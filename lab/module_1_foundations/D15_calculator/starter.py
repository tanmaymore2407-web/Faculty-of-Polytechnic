# D15 — Simple Calculator  (Module 1 mini-project)
#
# Read the full brief in problem.md.
# Write one function per operation, then the calculator() driver.
# Run the file to test.


def add(a, b):
    # 1. Return a + b
    pass


def subtract(a, b):
    # 1. Return a - b
    pass


def multiply(a, b):
    # 1. Return a * b
    pass


def divide(a, b):
    # 1. If b == 0, return the string "Error: cannot divide by zero"
    # 2. Otherwise return a / b
    pass


def modulo(a, b):
    # 1. If b == 0, return the string "Error: cannot divide by zero"
    # 2. Otherwise return a % b
    pass


def calculator():
    # 1. Ask for the first number  -> float(input("First number: "))
    # 2. Ask for the operator      -> input("Operator (+ - * / %): ")
    # 3. Ask for the second number -> float(input("Second number: "))
    # 4. Use if / elif / else to call the matching function:
    #       if op == "+":  result = add(a, b)
    #       elif op == "-": ...
    #       ...
    #       else:           print an "Unknown operator" message and stop
    # 5. Print the result like:  f"{a} {op} {b} = {result}"
    pass


if __name__ == "__main__":
    calculator()
