l=[]
n=int(input("Enter the number of elements in the list:"))

for i in range (n):
    print("Please enter the value no.",i+1," :",sep='',end='')
    val=int(input())            # Remove int() to make a list of strings,leave rest of prg. as it is.
    l.append(val)
print("The list is .........",l,sep="")

for k in range (n):
    for j in range (n):
        num=0
        if (l[k]<l[j]):         # If u replce this line with [ if (l[j]<l[k]) ], u get descending order.
            num=l[k]
            l[k]=l[j]
            l[j]=num
print("The sorted list is....",l,sep="")
