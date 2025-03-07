l=list(input("enter the list sep by spaces=").split())
for i in range(0,len(l),1) :
    l[i]=int(l[i])
n=len(l)
l1=[]
l1.append(1)    
a=1
for j in range(0,n-1,1):
    if(l[j+1]>l[j]):
        a=a+1
    else:
        a=1
    l1.append(a)
l2=[]
l2.append(1)
b=1
for k in range(n-1,0,-1):
    if(l[k-1]>l[k]):
        b=b+1
    else:
        b=1
    l2.append(b)
l2.reverse()    
l3=[]
for x in range(n):
    if(l1[x]>=l2[x]):
        l3.append(l1[x])
    else:
        l3.append(l2[x])
print(sum(l3))                        





            

