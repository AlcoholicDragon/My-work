n=int(input("Pls enter the total no. of rows :"))
m=int(input("Pls enter the total no. of columns :"))

matrix=[[0 for col in range (m)] for row in range (n)]
matrix1=[[0 for col in range (m)] for row in range (n)]
matrix2=[[0 for col in range (m)] for row in range (n)]

for i in range (n):
    print("For row no.",i+1," ............",sep="")
    for j in range (m):
        print("For cloumn no.",j+1," :",sep="",end="")
        val=int(input())
        matrix[i][j]=val

print("The matrix is ................")
for k in range (n):
    print(matrix[k])

print("The left triangle is ..........")
for x in range (n):
    for y in range (m):
        if (x>=y):
            matrix1[x][y]=matrix[x][y]
for z in range (n):
    print(matrix1[z])

print("The right triangle is ..........")
for a in range (n):
    for b in range (m):
        if (a+b==n-1 or a+b>=n):
            matrix2[a][b]=matrix[a][b]
for c in range (n):
    print(matrix2[c])
        
