#problem 1
def greet(): 
    n=input("enter your name:")
    a=int(input("enter your age:"))
    print("Hi",n + "!Next year you will be",a+1)
greet()
#problem 2
num=10
while True:
    uinp= int (input("1,2,3,4,5,6,7,8,9,10="))
    if uinp !=num:
        print("incorrect")
    else:
        print("correct ")
#problem 3  
n=5
student=[]
for x in range(n):
    name=input("Enter your name=")
    student.append(name)
print("student list")
print(student)
        
