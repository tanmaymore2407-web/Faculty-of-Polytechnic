#problem 1
num = 10

vnum = int(input("Give a number between 1 and 20: "))

if vnum == num:
    print("correct")
else:
    print("wrong gess")

#problem 2
num = 10

vnum = int(input("Give a number between 1 and 20: "))

if vnum == num:
    print("correct")
elif vnum > num:
    print("high")
else:
    print("low")

#problem 3
def guess_number():
    num = 10 

    while True:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess == num:
            print("Right")
            break
        else:
            print("Wrong")

guess_number()
