def ser(n,x,s):
    if (n!=0):
        if(n>1):
            s+=int(x**n/n)
            ser(n-1,x,s)
    if(n==0):
        print(s)
        return 
ser(4,2,1)
