l=list(input("enter the list sep by spaces=").split())
for i in range(0,len(l),1) :
    l[i]=int(l[i])
n=len(l)  
k=int(input("rotate by how many spaces="))
p=[]  
for j in range(0,len(l),1):
    p.append(l[(j+n-k)%n])  
print("list after rotating=",p)
