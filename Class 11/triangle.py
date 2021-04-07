l=int(input("Enter the lentgh of the triangle:"))
n=l+1
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
