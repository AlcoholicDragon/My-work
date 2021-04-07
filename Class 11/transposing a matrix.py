n=int(input("Please enter the total no. of rows:"))
m=int(input("Please enter the total no. of columns:"))

matrix=[[0 for col in range (m)] for row in range (n)]
matrixb=[[0 for col in range (n)] for row in range (m)]

print("For matrix ................")
for i in range (n):
    print("For row no.",i+1," :",sep="")
    for j in range (m):
        print("Please enter value no.",j+1," :",sep="",end="")
        num=int(input())
        matrix[i][j]=num
print("The matrix is ....................")
for k in range (n):
    print(matrix[k])

print("The transposed matrix is ................")
for x in range (m):
    for y in range (n):
        matrixb[x][y]=matrix[y][x]
for z in range (m):
    print(matrixb[z])
