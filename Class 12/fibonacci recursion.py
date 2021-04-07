def fibo(x):
    def fibo_upper(x):
        if (x==1 or x==0):
            return(1)
        elif (x < 0):
            return "Please enter a positive number."
        else:
            return(fibo_upper(x-1)+fibo_upper(x-2))
    print(0)
    for i in range(x):
        print(fibo_upper(i))
x=int(input("Please enter a number:"))
fibo(x)
    
