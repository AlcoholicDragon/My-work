l=[]
def isprimeinr(s,r):
    def isprime(a,s=2):
        if (a>1 and s>=2):
            if(a%s!=0):
                isprime(a,s+1)
            if (a==s):
                l.append(a)
                return
            if (a%s==0):
                return
        else:
            return
    isprime(s)
    if (s==r):
        return
    else:
        isprimeinr(s+1,r)
isprimeinr(2,20)
for i in l:
    print(i,"is a prime number.")
