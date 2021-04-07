l=[]
n=int(input("Pls enter the No. of elements of the list (it should be even):"))

for i in range (n):
    print("Pls enter value No.",i+1," :",sep="",end="")
    num=int(input())
    l.append(num)
print(l)

a=int(n/2)
for j in range (a):
    num1=l[0]
    del(l[0])
    l.append(num1)
print(l)
