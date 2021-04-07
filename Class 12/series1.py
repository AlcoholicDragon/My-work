#Q29
def ser(n,s):
    if (n!=0):
        s+=1/n
        ser(n-1,s)
    if(n==0):
        print(s)
        return
ser(4,0)

