def perfect(a):
    l=[]
    def factors(a,s=1):
        if (a==s):
            return
        if (a%s==0):
            l.append(s)
            factors(a,s+1)
        if (a%s!=0):
            factors(a,s+1)
    factors(a)
    k=sum(l)
    if (k==a):
        return True
    else:
        return False
print(perfect(496))
