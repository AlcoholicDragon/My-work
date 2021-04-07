d={}
n=int(input("Pls enter the total no. of elements:"))

for i in range (n):
    it=str(input("Pls enter the name of the item:"))
    pr=float(input("Pls enter the price of the given item:"))
    d[it]=pr

k=list(d.keys())
v=list(d.values())
l=[]+v
for j in range (3):
    x=0
    for b in v:
        if (b!=max(l)):
            x+=1
        else:
            print(k[x],":",b)
            l.remove(b)
            break
