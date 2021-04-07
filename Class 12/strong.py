l=[]
def strong(a):
    def fact(x):
        if (x==0):
            return 1
        else:
            return(x*fact(x-1))
    if (a==0):
        return 0
    else:
        l.append(fact(a%10))
        strong(a//10)
    s=sum(l)
    if (a==s):
        return True
    else:
        return False
print(strong(145))
