s=int(input("starting number:"))
e=int(input("final number:"))
n=int(input("decremention by:"))

e-=n
for i in range (s,e,-n):
    for x in range (s,i-n,-n):
        print(x,end=' ')
    print()
