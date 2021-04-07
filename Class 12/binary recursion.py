#Q5(recursion)
l=[]
def binary(a):
    if (a==0):
        return
    else:
        b=a%2
        l.append(b)
        binary(a//2)
binary(15)
l.reverse()
Str=""
for i in l:
    Str+=str(i)
print(Str)

