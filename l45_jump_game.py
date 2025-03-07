l=list(input("enter the list sep by spaces=").split())
for i in range(0,len(l),1) :
    l[i]=int(l[i])
farthest=0
jumps=0
current=0
for i in range(0,len(l)-1,1):
    if((i+l[i])>farthest):
        farthest=i+l[i]
        
    if(i==current):
        current=farthest
        jumps=jumps+1
print("the jumps required is=",jumps)                