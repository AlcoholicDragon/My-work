# Write a prg to input a number and print all the factors of that number

num=int(input("Pls enter the number that is to be factorised:"))
c=num
l=[]
while (num != 1):
    for i in range (2,c):
        if (num%i == 0):
            l.append(i)
            num=int(num/i)
            break
print("The factors are ",end="")
for j in range (len(l)):
    print(l[j],end=",")
