l=[]
n=int(input("Enter the number of elements in the list:"))

for i in range (n):
    print("Please enter the value no.",i+1," :",sep='',end='')
    val=int(input())         # Remove int() to make a list of strings,leave rest of prg. as it is.
    l.append(val)
print("The list is .........",l,sep="")

for k in range (n):
    for j in range (n-k):
        num=0
        if (j<n-1):
            if (l[j]>l[j+1]):
                num=l[j]
                l[j]=l[j+1]
                l[j+1]=num
print("The sorted list is .......",l,sep="")

