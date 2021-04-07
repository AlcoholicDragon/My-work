#A1
#i
def S_O_T(a,b,c):
    return a+b+c
print(S_O_T(1,2,3))
#ii
def great(a,b):
     if (a>b):
         return a
     else:
         return b
print(great(1,3))
#iii
def area(l,b):
    return l*b
print(area(9,4))
#A2
#i
def rev_int(b):
   # b=str(b)
    b=str(b)
    return b[::-1]
print(rev_int(123))
#ii
def S_O_D(b):
    s = 0
    while b:
        s += b % 10
        b //= 10
    return s
print(S_O_D(4568))
#iii
def C_O_D(b):
  return len(str(abs(b)))
print(C_O_D(5456))
#iv
def fact(b):
    if b == 0:
        return 1
    else:
        return b * fact(b-1)
print(fact(4))
#v
def HCF(a,b):
    if a>b:
        x=a
    else:
        x=b
    for i in range(1,x):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
print(HCF(4,8))
#vi
def LCM(a,b):
    if a>b:
        x=a
    else:
        x=b
    for j in range(x,a*b):
        if j%a==0 and j%b==0:
            lcm =j
            break
    return lcm
print(LCM(4,8))
#A3
#i
def isarmst(b):
    sum = 0
    num=b
    while b > 0:
        digit = b % 10
        sum += digit ** 3
        b //= 10
    print(b)
    if num == sum:
        return True
    else:
        return False

print(isarmst(5347))

#ii
def isprime(b):
    if b > 1:
       for i in range(2,b):
           if (b % i) == 0:
               return False
               break
       else:
           return True
    else:
        return False
print(isprime(3))
