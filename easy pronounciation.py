t=int(input())
vowels='aeiou'
for i in range(t):
    n=int(input())
    s=str(input())
    count=0
    for alpha in s:
        if s[s.index(alpha)] not in vowels:
            count+=1
        elif (count<4):
            count=0
        
    if count>=4:
        print("NO")
    else:
        print("YES")
