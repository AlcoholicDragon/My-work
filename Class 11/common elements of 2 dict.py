# Write a prg. to take 2 dictionaries as an input and print the common elements from both the
# dictionaries

d1,d2={},{}
n=(int(input("Enter the number of elements:")))

print("For dictionary 1.........")
for i in range (n):
    key1=input("Enter the key:")
    value1=input("Enter the given key's value:")
    d1[key1]=value1

print("For dictionary 2.........") 
for j in range (n):
    key2=input("Enter the key:")
    value2=input("Enter the given key's value:")
    d2[key2]=value2

for k in d1:
    if (k in d2):
        print(k,"is present in both the dictionaries.")
