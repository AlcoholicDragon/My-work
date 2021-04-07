m=int(input("Enter the no. of columns :"))
n=int(input("Enter the no. of rows :"))

matrix1=[[0 for col in range (m)] for row in range (n)]
matrix2=[[0 for col in range (m)] for row in range (n)]
matrix3=[[0 for col in range (m)] for row in range (n)]

print("\nFor matrix 1")
for i in range (n):
    print("For row no.",i+1,sep="")
    for j in range (m):
        print("Value no.",j+1," :",sep="",end="")
        num1=int(input())
        matrix1[i][j]=num1
print("\nMatrix 1 is ...........")
for x in range (n):
    print(matrix1[x])

print("\nFor matrix 2")
for a in range (n):
    print("For row no.",a+1,sep="")
    for b in range (m):
        print("Value no.",b+1," :",sep="",end="")
        num2=int(input())
        matrix2[a][b]=num2
print("\nMatrix 2 is ...........")
for y in range (n):
    print(matrix2[y])

print("\nMatrix 3 is the sum of matrix 2 and matrix 1")
for p in range (n):
    for q in range(m):
        matrix3[p][q]=matrix2[p][q]+matrix1[p][q]
print("Matrix 3 is ...........")
for z in range (n):
    print(matrix3[z])
