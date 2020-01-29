def myfun(source,dest):
   if(source=='tvk' and dest=='venus'):
       print("the bill amt is 100")
   elif(source=='tvk' and dest=='perambur'):
       print("the bill amt is 300")
   elif(source=='venus' and dest=='perambur'):
        print("the bill amt is 150")
   

source=raw_input("enter the source")
dest=raw_input("enter the destination")
n=myfun(source,dest)

