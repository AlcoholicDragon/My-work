#Q2(recursion)
l=[]
def fact(ns,nn):
    f=1
    if (ns<=nn):
        l.append(ns)
        fact (ns+1,nn)
    if (ns>nn):
        return
fact(1,5)
f=1
for i in range (1,len(l)+1):
    f*=i
print(f)
