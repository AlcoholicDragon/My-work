#Q34
l=[]
def coll(s):
    print(s)
    if (len(l)==0):
        l.append(s)
        coll(l[len(l)-1])
    elif (s==1):
        print(True)
    else:
        if (s%2==0):
            l.append(int(s/2))
            coll(l[len(l)-1])
        elif (l[len(l)-1]%2!=0):
            l.append(int(3*s)+1)
            coll(l[len(l)-1])

coll(12)