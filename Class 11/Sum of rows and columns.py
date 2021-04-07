n=int(input("Please enter the total no. of rows:"))
m=int(input("Please enter the total no. of columns:"))

matrix=[[0 for col in range (m)] for row in range (n)]
n_matrix=[[0 for col in range (m)] for row in range (n)]

print("For the matrix ..........")
for i in range (n):
    print("For row no.",i+1," :",sep="")
    for j in range (m):
        print("Please enter value no.",j+1," :",end="",sep="")
        num=int(input())
        matrix[i][j]=num
print("The matrix is .............")
for k in range (n):
    print(matrix[k])


print("For rows ............")
for d in range (n):
    print("Sum of elements of row no.",d+1," : ",sum(matrix[d]),sep="")

print("For columns ............")
for x in range (n):
    for y in range (m):
        n_matrix[x][y]=matrix[y][x]
for z in range (n):
    print("Sum of elements of column no.",z+1," : ",sum(n_matrix[z]),sep="")
