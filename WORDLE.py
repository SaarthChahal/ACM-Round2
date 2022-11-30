T=int(input())
for i in range(T):
    S=(input())
    T=(input())
    for j in range (5):
        m=''
        if S[j]==T[j]:
            m+='G'
        else:
            m+='B'
        print(m,end='')
    print('')
