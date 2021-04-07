l,nl=[],[]
def primef(a):
    def factors(a,s=1):
        if (a==s):
            return
        if (a%s==0):
            l.append(s)
            factors(a,s+1)
        if (a%s!=0):
            factors(a,s+1)
    def isprime(a,s=2):
        if (a>1 and s>=2):
            if(a%s!=0):
                isprime(a,s+1)
            if (a==s):
                nl.append(a)
                return
            if (a%s==0):
                return
        else:
            return
    factors(a)
    for i in l:
        isprime(i)
primef(28)
print(nl)
