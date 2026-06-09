# D14 — Refactor: Spaghetti -> Clean
#
# Read the full brief in problem.md.
#
# This script WORKS. Run it and you'll see a tidy report card for three
# students. But the code is "spaghetti": one long flat block with the SAME
# calculation copy-pasted three times, magic numbers, and unclear names.
#
# Your job: refactor it into clean, named functions WITHOUT changing the
# output. Run example_run.txt-style output before AND after to prove it's
# identical. Look for the `# TODO:` comments — they mark the smells.


# TODO: these three "averages" use the magic number 3 everywhere.
#       The pass mark 35 and the distinction mark 75 are also magic numbers.

print("===== REPORT CARD =====")

# ----- student 1 -----
# TODO: this whole block is copy-pasted below for student 2 and student 3.
#       Extract a function, e.g. print_report(name, m1, m2, m3).
n = "Aarav"
a = 40
b = 55
c = 70
t = a + b + c
av = t / 3
print("Name: " + n)
print("Marks: " + str(a) + ", " + str(b) + ", " + str(c))
print("Total: " + str(t) + " / 300")
print("Average: " + str(round(av, 2)))
# TODO: 35 and 75 are magic numbers. Give them names.
if av < 35:
    print("Result: FAIL")
elif av >= 75:
    print("Result: PASS (Distinction)")
else:
    print("Result: PASS")
print("-----------------------")

# ----- student 2 -----
n = "Diya"
a = 30
b = 28
c = 33
t = a + b + c
av = t / 3
print("Name: " + n)
print("Marks: " + str(a) + ", " + str(b) + ", " + str(c))
print("Total: " + str(t) + " / 300")
print("Average: " + str(round(av, 2)))
if av < 35:
    print("Result: FAIL")
elif av >= 75:
    print("Result: PASS (Distinction)")
else:
    print("Result: PASS")
print("-----------------------")

# ----- student 3 -----
n = "Kabir"
a = 88
b = 91
c = 79
t = a + b + c
av = t / 3
print("Name: " + n)
print("Marks: " + str(a) + ", " + str(b) + ", " + str(c))
print("Total: " + str(t) + " / 300")
print("Average: " + str(round(av, 2)))
if av < 35:
    print("Result: FAIL")
elif av >= 75:
    print("Result: PASS (Distinction)")
else:
    print("Result: PASS")
print("-----------------------")
