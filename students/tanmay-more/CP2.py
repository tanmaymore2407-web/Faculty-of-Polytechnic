#problem no 1
def ask_text():
    while True:
        name = input("What is your name? ")
        if name == "":
            return("Can't be empty. Try again.")
        else:
            return(name)
            break
    while True:
        sub_name = input("Enter subject name? ")
        if sub_name == "":
            return("Can't be empty. Try again.")
        else:
            return(sub_name)
            break
