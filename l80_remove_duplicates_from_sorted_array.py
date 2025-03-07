s=input("enter the array=").split()
s.sort()
s="".join(s)
for j in range(0,len(s),1):
    c=s.count(s[j])
    if(c>=3):
        s=s.replace(s[j:j+c],s[j:j+2])
    if((j+1)==len(s)):
        l=list(s)
        print("the final array=",l)
        break

      
