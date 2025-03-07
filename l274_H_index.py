def fn(l,n):
    c=0
    for i in range(0,len(l),1):
        if(l[i]>=n):
            c=c+1
    if(c>=n):
        return 1
    else:
        return 0
l=list(input("enter the list sep by spaces=").split())
for i in range(0,len(l),1) :
    l[i]=int(l[i])
for j in range(1,len(l)+1,1):
    if(fn(l,j)==0):
        print("the H-index is=",j-1)
        break
    