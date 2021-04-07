n=int(input("Please enter the total no. of rows:"))
m=int(input("Please enter the total no. of columns:"))

matrix=[]
r_matrix=[[0 for col in range (m)] for row in range (n)]

for i in range (n):
    print("For row no.",i+1," :",sep="")
    l=[]
    for j in range (m):
        print("For value no.",j+1," :",end="",sep="")
        num=int(input())
        l.append(num)
    matrix.append(l)
print("The matrix is .............")
for k in range (n):
    print(matrix[k])
print("For rows ..............")
for a in range (n):
    if (a%2 == 0):
        print("For row no.",a+1," :",sum(matrix[a]),sep="")
print("For columns ............................")
for b in range (n):
    for c in range (m):
        r_matrix[b][c]=matrix[c][b]
for d in range (n):
    if (d%2 == 0):
        print("For column no.",d+1," :",sum(r_matrix[d]),sep="")
