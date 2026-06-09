# D12 — Geometry Helpers
#
# Read the full brief in problem.md.
# Implement both functions below. Run the file to test.


def rectangle(width, height):
    # 1. Compute area = width * height
    # 2. Compute perimeter = 2 * (width + height)
    # 3. Return BOTH as a tuple: return area, perimeter
    pass


def circle(radius, pi=3.14159):
    # Note the default parameter: pi=3.14159
    # 1. Compute area = pi * radius * radius
    # 2. Compute circumference = 2 * pi * radius
    # 3. Return BOTH as a tuple: return area, circumference
    pass


if __name__ == "__main__":
    # Unpack the returned tuple into two names:
    a, p = rectangle(3, 4)
    print("Rectangle area:", a)        # 12
    print("Rectangle perimeter:", p)   # 14

    print()  # blank line between the two problems

    a, c = circle(2)                   # uses default pi = 3.14159
    print("Circle area:", round(a, 2))           # 12.57
    print("Circle circumference:", round(c, 2))  # 12.57

    a, c = circle(2, pi=3.14)          # override the default pi
    print("Circle area (pi=3.14):", round(a, 2))           # 12.56
    print("Circle circumference (pi=3.14):", round(c, 2))  # 12.56
