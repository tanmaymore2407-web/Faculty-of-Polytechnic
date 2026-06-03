t=0
n=1
while n<=10:
    t+=n
    n+=1
print (t) 
#problem
a=4
b=9
c=19
for num in [a, b, c]:
    if num % 3 == 0:
    print(num, "is divisble by 3") 
else:
    print(num, "is not divisble by 3") 

#problem
l=[1, 2,3,4,5,6]
l.pop(0) 
l.pop(2) 
l.pop(4) 
print(l) 
#problem
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1) 
l.pop(2) 
print(l) 
#problem
l=[1,2,3,4,5,6]
l.pop(4) 
l.pop(2) 
l.pop(0) 
print(l) 
