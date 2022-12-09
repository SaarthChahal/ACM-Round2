t=int(input())
for i in range(t):
    cook_list=[]
    c_ct=0 #Exactly_one
    s_ct=0 #Exactly_one
    e_ct=0 #Exactly_one
    em_ct=0 #atleast 1
    m_ct=0 #atleast 1
    mh_ct=0 #atleast 1
    h_ct=0 #atleast 1
    n=int(input())
    for j in range(n):
        contest=str(input())
        cook_list.append(contest)
        for s in cook_list:
            if s.lower()=="cakewalk":
                c_ct+=1
            elif s.lower()=="simple":
                s_ct+=1
            elif s.lower()=="easy":
                e_ct+=1
            elif s.lower()=="easy-medium":
                em_ct+=1
            elif s.lower()=="medium":
                m_ct+=1
            elif s.lower()=="medium-hard":
                mh_ct+=1
            elif s.lower()=="hard":
                h_ct+=1
    
    if c_ct>=1 and s_ct>=1 and e_ct>=1:
        if em_ct+m_ct>=1 and mh_ct+h_ct>=1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")