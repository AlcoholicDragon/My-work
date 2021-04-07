print("-------------------------------THE MATRIX-------------------------------")
print("""WELCOME TO THE MATRIX
HERE YOU WILL BE GIVEN A MATRIX AND YOU GET TO SELECT THE DIMENSIONS OF THE
MATRIX AS WELL AS THE STRUCTURE.
LET'S GET STARTED !!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
n=int(input("Please enter the dimensions of the matrix (It will be in NxN format):"))
print("""Please select the type of shape you want:
         1.Simple Matrix 
         2.Upper right triangle
         3.Upper left triangle
         4.Lower right triangle
         5.Lower left triangle
         6.Cross
         7.Custom selection
         8.Quit""")
l=[1,2,3,4,5,6,7,8]
while True:
    opt=int(input("Please enter your choice (1-8):"))
    if (opt not in l):
        print("Please enter a valid option.")
    elif (opt==8):
        m=str(input("Are you sure you want to quit?(yes/no) "))
        if (m=="YES" or m=="yes"):
            print("Thank you for your coooperation")
            break
        break
    elif (opt==1):
        o=input("Please enter the character:")
        matrix1=[[o for col in range (n)] for row in range (n)]
        print("The matrix is ...........")
        for i in range (n):
            print(matrix1[i])
    elif (opt==2):
        o=input("Please enter the character for the triangle:")
        matrix2=[[" " for col in range (n)] for row in range (n)]
        for i in range (n):
            for j in range (n):
                if (i<=j):
                    matrix2[i][j]=o
        print("The upper right triangle is ........")
        for k in range (n):
            print(matrix2[k])
    elif (opt==3):
        o=input("Please enter the character for the triangle:")
        matrix3=[[" " for col in range (n)] for row in range (n)]
        for i in range (n):
            for j in range (n):
                if (i+j<=n-1):
                    matrix3[i][j]=o
        print("The upper left triangle is ........")
        for k in range (n):
            print(matrix3[k])
    elif (opt==4):
        o=input("Please enter the character for the triangle:")
        matrix4=[[" " for col in range (n)] for row in range (n)]
        for i in range (n):
            for j in range (n):
                if (i+j>=n-1):
                    matrix4[i][j]=o
        print("The lower right triangle is ........")
        for k in range (n):
            print(matrix4[k])
    elif (opt==5):
        o=input("Please enter the character for the triangle:")
        matrix5=[[" " for col in range (n)] for row in range (n)]
        for i in range (n):
            for j in range (n):
                if (i>=j):
                    matrix5[i][j]=o
        print("The lower left triangle is ........")
        for k in range (n):
            print(matrix5[k])
    elif (opt==6):
        o=input("Please enter the character for the cross:")
        matrix6=[[" " for col in range (n)] for row in range (n)]
        for i in range (n):
            for j in range (n):
                if (i==j or i+j==n-1):
                    matrix6[i][j]=o
        print("The cross is ............")
        for k in range (n):
            print(matrix6[k])
    elif (opt==7):
        o=input("Please enter the character for input:")
        matrix7=[[" " for col in range (n)] for row in range (n)]
        while True:
            ask=str(input("Do you want to give an index? (yes/no) "))
            if (ask=="YES" or ask=="yes"):
                print("Please enter column no.(0-",n-1,") :",sep="",end="")
                col=int(input())
                print("Please enter row no.(0-",n-1,") :",sep="",end="")
                row=int(input())
                matrix7[col][row]=o
            else:
                print("Thank you for your cooperation.")
                break
        print("Your custom selected design is .........")
        for k in range (n):
            print(matrix7[k])
