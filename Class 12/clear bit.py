def clrbit(a):
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
        for i in range (len(l)):
            if (l[i]==1):
                del(l[i])
                break
        Str=""
        l.reverse()
        for i in range (len(l)):
            Str+=str(l[i])
        print(Str)
print(clrbit(11))
      
