n=int(input("Please enter the total no. of rows:"))
m=int(input("Please enter the total no. of columns:"))
matrix=[[0 for col in range (m)] for row in range (n)]

for i in range (n):
    print("FOR ROW NO.",i+1,":",sep="")
    for j in range (m):
        print("ENTER VALUE NO.",j+1,":",end="",sep="")
        num=int(input())
        matrix[i][j]=num
def sod(a):
    r_list=[]
    n=len(a)
    m=len(a[0])
    
    for k in range (n):
        for f in range (m):
            if (k==f):
                val=matrix[k][f]
                r_list.append(val)
    print(r_list)
    print("SUM OF DIAGONAL FROM LEFT TO RIGHT IS .............",sum(r_list))

    nr_list=[]

    for s in range (n):
        for r in range (m):
            if (s+r==n-1):
                nval=matrix[s][r]
                nr_list.append(nval)
    print(nr_list)
    print("SUM OF DIAGONAL FROM RIGHT TO LEFT IS .............",sum(nr_list))
sod(matrix)
