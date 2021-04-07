s=str(input("Please enter the string:"))
a=str(input("Please enter the string:"))
for i in range (len(s)):
    for j in range (len(s)):
        if (a==s[i:j]):
            print("The substring is [",i,":",j,"].",sep="")
