d,d1,d2,d3={},{},{},{}

n1=int(input("Pls enter total no. of items in dict 1:"))
n2=int(input("Pls enter total no. of items in dict 2:"))
n3=int(input("Pls enter total no. of items in dict 3:"))

print("For dict 1 ........")
for a in range (n1):
    key1=input("Pls enter the name of the item:")
    val1=int(input("Pls enter the given item's price:"))
    d1[key1]=val1

print("For dict 2 ........")
for b in range (n2):
    key2=input("Pls enter the name of the item:")
    val2=int(input("Pls enter the given item's price:"))
    d2[key2]=val2

print("For dict 3 ........")
for c in range (n3):
    key3=input("Pls enter the name of the item:")
    val3=int(input("Pls enter the given item's price:"))
    d3[key3]=val3

d.update(d1)
d.update(d2)
d.update(d3)
print(d)
