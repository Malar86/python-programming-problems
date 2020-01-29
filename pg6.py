l=['mars','earth','universe','stars','astroids','blackhole']
n=15
alpha=''
while n>0:
    ip=raw_input("enter alphabets related to space")
    for i in ip:
        alpha=str(alpha)+i
        print alpha
        if alpha in l:
            print "success"
            break
        
            
       
            
        
          

