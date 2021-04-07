n=int(input("ENTER THE NUMBER OF ROWS:"))
m=int(input("ENTER THE NUMBER OF COLUMNS:"))
matrix=[[0 for col in range (m)]for row in range (n)]
print("ENTER MATRIX VALUES--->")
for i in range (n):
      print("ENTER THE VALUES FOR ROW",i+1," ---->")
      for j in range (m):
            num=int(input("ENTER VALUE:"))
            matrix[i][j]=num
print("THE MATRIX IS...........")
for r in range (len(matrix)):
      print(matrix[r])
      print('\t')
Sum=0
for x in range(n):
      for y in range (m):
            if (matrix[x][y]%2==0):
                  Sum+=matrix[x][y]
print(Sum)
