lg=list(input("enter the gas sep by spaces=").split())
for i in range(0,len(lg),1) :
    lg[i]=int(lg[i])
lc=list(input("enter the cost sep by spaces=").split())
for i in range(0,len(lc),1) :
    lc[i]=int(lc[i])
n=len(lg) 
   
for i in range(n):
    p=0
    for j in range(i,i+n,1):
        p=p+lg[j%n]-lc[j%n]
        if(p<0):
            c=1
            break
        else:
            c=0
    if(c==0):
        print("the station is=",i)
        exit()
print("the station is=",-1)                




        
        

