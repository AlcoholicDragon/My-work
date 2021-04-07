def isarm(a):
    Sum=0
    num=a
    if (a==0):
        if (Sum==num):
            print("True")
        else:
            print("False")
    else:
        Sum+=(a%10)**3
        isarm(a//10)
print(isarm(371))
