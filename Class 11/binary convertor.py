num=int(input("Enter the number to be converted into binary:"))
num1=list()
while num!=0:
    a=str(num%2)
    num1.append(a)
    num=num//2
num1.reverse()
for i in range (len(num1)):
    binary=''
    s=str(num1[i])
    print(s,end='')

