def fn(s):
    s1=set(s)
    return len(s1)==len(s)
s=input("enter the string here=")
length=0
i=0
for j in range(len(s)):
    for x in range(i,j):
        if not (fn(s[i:j+1])):
            i=i+1
        else:
            break
    length=max(length,j-i+1)
print("the max length of non repeating string is=",length)    


        
              
            
