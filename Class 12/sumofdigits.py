l=[]
def Sum(a):
    if(a==0):
        return
    else:
        l.append(a%10)
        Sum(a//10)
Sum(123)
s=0
for i in l:
    s+=i
print(s)
