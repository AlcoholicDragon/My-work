n=int(input("ENTER THE NUMBER OF ROWS:"))
m=int(input("ENTER THE NUMBER OF COLUMNS:"))
matrix=[[0 for col in range (m)] for row in range (n)]

for i in range (n):
    print("FOR ROW NO.",i+1,":",sep="")
    for j in range (m):
        print("ENTER VALUE NO.",j+1,":",end="",sep="")
        num=int(input())
        matrix[i][j]=num

print("FOR ROWS..........")
for k in range (n):
    Row=matrix[k]
    print("SUM OF ROW NO.",k+1,"is....",sum(Row))

r_matrix=[[0 for col in range (m)] for row in range (n)]
for x in range (n):
    for y in range (m):
        r_matrix[x][y]=matrix[y][x]

print("FOR COLUMNS..........")
for z in range (n):
    Column=r_matrix[z]
    print("SUM OF COLUMN NO.",z+1,"is....",sum(Column))
