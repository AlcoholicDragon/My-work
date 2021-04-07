def isprime(a,s=2):
    if (a>1 and s>=2):
        if(a%s!=0):
            isprime(a,s+1)
        if (a==s):
            print("True")
            return
        if (a%s==0):
            print("False")
            return
    else:
        return
isprime(5)
