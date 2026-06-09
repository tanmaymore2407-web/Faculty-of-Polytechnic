# D6 — Grade Classifier + Leap Year
#
# Read the full brief in problem.md.
# These are pure functions: they RETURN a value, they don't print.
# Implement both functions below. Run the file to test.

def classify_grade(score):
    # 1. If score >= 90, return "A"
    # 2. elif score >= 80, return "B"
    # 3. elif score >= 70, return "C"
    # 4. elif score >= 60, return "D"
    # 5. else, return "F"
    pass


def is_leap_year(year):
    # 1. Divisible by 4  -> year % 4 == 0
    # 2. ...AND (not divisible by 100  OR  divisible by 400)
    # 3. Return the combined True/False result
    pass


if __name__ == "__main__":
    print(classify_grade(85))  # B
    print(is_leap_year(2000))  # True
    print(is_leap_year(1900))  # False
