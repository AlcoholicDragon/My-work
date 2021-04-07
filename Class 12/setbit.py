def setbit(a):
    if (a==0):
        return 0
    else:
        ct=0
        l=[]
        def binary(a):
            if (a==0):
                return
            else:
                b=a%2
                l.append(b)
                binary(a//2)
        binary(a)
        for i in l:
            if (i==1):
                ct+=1
        return ct
print(setbit(15))
