import random
n=5
while n>0:
  a=int(input("enter a number"))
  b=random.randrange(0,5)
  if(a==b):
      print("you won")
      break
  else:
      print("you lost")

