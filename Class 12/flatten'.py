#Q3(recursion)
l=[[1,2,3],[4,5,6],[7,8,9]]
q,s=[],0
def flat(l,q,s):
    if(s<len(l)):
        q+=l[s]
        flat(l,q,s+1)
flat(l,q,0)
print(q)
