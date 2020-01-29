import random

a='0->stone'
print(a)
b='1->paper'
print(b)
c='2->scissor'
print(c)
n=8
while n>0:
    ip=int(input("enter a number"))
    b=random.randrange(0,3)
    if(ip==0 and b==0):
        print("try again")
    elif(ip==1 and b==1):
        print("try again")
    elif(ip==2 and b==2):
        print("try again")
    elif(ip==0 and b==1 or ip==1 and b==2):
        print("you lost")
    elif(ip==2 and b==1):
        print("you won")
    elif(ip==2 and b==0):
        print("you lost")
    elif(ip==1 and b==0):
        print("you won")
    elif(ip==0 and b==2):
        print("you won")
    
