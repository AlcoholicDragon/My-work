l1,l2=[],[]
n=int(input("Pls enter the number of elements in list1:"))
m=int(input("Pls enter the number of elements in list2:"))

print("\nFor list 1 .........")
for i in range(n):
    print("Pls enter the value no.",i+1," :",end="",sep="")
    val1=int(input())
    l1+=[val1]

print("\nFor list 2 .........")
for j in range(m):
    print("Pls enter the value no.",j+1," :",end="",sep="")
    val2=int(input())
    l2+=[val2]

def insertion(l):
    x=0
    for a in l:
        x+=1
    for y in range (x):
        for z in range (x):
            num=0
            if (l[y]<l[z]):         
                num=l[y]
                l[y]=l[z]
                l[z]=num
    print(l,sep='')

print("List 1 is ........",end="")
insertion(l1)
print("List 2 is ........",end="")
insertion(l2)

l3=l1+l2

print("The combined sorted list is ..........",end="")
insertion(l3)

l4=[]

for q in l3:
    if q not in l4:
        l4.append(q)
print("The new combined list with no repeated elements is ..........",l4)

