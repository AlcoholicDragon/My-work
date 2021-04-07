def ser(n,u,s=1,su=0):
    def fact(n,p=1):
        if (n != 0):
            p*=n
            return fact(n-1,p)
        else:
            return p
    if (n==0):
        return 0
    elif (n>=s):
        su+=(u**s)/fact(s+1)
        print((u**s)/fact(s+1))
        return(ser(n,u,s+1,su))
    elif(n<s):
        return su
print(ser(4,1))
        
