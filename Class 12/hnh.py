l=[]
n=int(input("Please the lentgh of the list:"))
for i in range (n):
    num=input("Please enter a value:")
    l.append(num)
q=[]
def hnh(l):
    n=len(l)//2
    for i in range(n,len(l)):
        q.append(l[i])
    for i in range (n):
        q.append(l[i])
    return q

print(hnh(l))
