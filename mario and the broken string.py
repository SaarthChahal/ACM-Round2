
t=int(input()) #number of test cases

for count in range(t):
    n=int(input()) #length of string
    s=str(input()) #input string
    s1=s[:int(len(s)/2)]
    s2=s[int(len(s)/2):]
    
    if s1+s2==s and s2+s1==s:
        print("YES")
    else:
        print("NO")

