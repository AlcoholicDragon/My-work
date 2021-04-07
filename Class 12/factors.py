l=[]
def factors(a,s=1):
    if (a==s):
        return
    if (a%s==0):
        l.append(s)
        factors(a,s+1)
    if (a%s!=0):
        factors(a,s+1)
a=int(input("Please enter a number:"))
factors(a)
print("The factors of",a,"are",end=" ")
for i in l:
    print(i,end=",")
