l=list(input("enter the height sep by spaces=").split())
for x in range(0,len(l),1) :
    l[x]=int(l[x])
c=0    
for y in range(1,max(l)+1,1):
    for i in range(0,len(l),1):
        if(l[i]>=y):
            break
    for j in range(len(l)-1,-1,-1):
        if(l[j]>=y):
            break
    if(i==j):
        break
    for k in range(i,j+1,1):
        if(l[k]<y):
            c=c+1
print("the trapped rain water is=",c)            

