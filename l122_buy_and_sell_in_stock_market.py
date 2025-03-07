l=list(input("enter the prices in the market day by day=").split())
for i in range(0,len(l),1) :
    l[i]=int(l[i])
p=0    
for j in range(0,len(l),1):
    if((j+1)==len(l)):
        break
    elif(l[j+1]>l[j]):
        p=p+(l[j+1]-l[j])
print("the maximum profit=",p)
