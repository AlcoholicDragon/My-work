m=int(input("Please enter the total no. of rows:"))
n=int(input("Please enter the total no. of columns:"))

matrix=[[0 for col in range (m)] for row in range (n)]
r_matrix=[[0 for col in range (m)] for row in range (n)]

for i in range (n):
    print("For row no.",i+1," :----------",sep="")
    for j in range (m):
        print("For value no.",j+1," :",sep="",end="")
        val=int(input())
        matrix[i][j]=val
print("The matrix is ........")

for k in range (n):
    print(matrix[k])

print("The matrix with alternating elements is ...............")
for x in range (n):
    for y in range (m):
        if (x%2 == 0):
            if (y%2 == 0):
                r_matrix[x][y]=matrix[x][y]
        elif (x%2 != 0):
            if (y%2 != 0):
                r_matrix[x][y]=matrix[x][y]

for z in range (n):
    print(r_matrix[z])
            
