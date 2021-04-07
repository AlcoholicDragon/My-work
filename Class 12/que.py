q=[]
def dq(q):
    if (len(q)==0):
        return("Underflow")
    else:
        del(q[0])
print(dq(q))
        
