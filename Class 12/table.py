def table (a,s=1):
    if (s<=10):
        print(a,"*",s,"=",a*s,sep="")
        table(a,s+1)
table(57)
