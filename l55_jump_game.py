l=list(input("enter the list sep by spaces=").split())
s="".join(l)
c=s.count("0")
d=0
if(c==0):
    print("TRUE")    
else:
    if(c==1):
        i=s.find("0")
        for j in range(0,i,1):
            if(int(s[j])>(i-j)):
                d=d+1
        if(d>=1):
            print("TRUE")
        else:
            print("FALSE")            
                      
