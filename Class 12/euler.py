#Q31
nl=[1]
def euler(s,n):
    Sum=0
    if (s<=n):
        l=[]
        def fact(ns,nn):
            if (ns<=nn):
                l.append(ns)
                fact (ns+1,nn)
            if (ns>nn):
                return
        fact(1,s)
        f=1
        for i in range (1,len(l)+1):
            f*=i
        nl.append(1/f)
        euler(s+1,n)
    if (s>n):
        return
n=int(input("Please enter a number:"))
euler(1,n)
e=0
for i in nl:
    e+=i
print(e)
