import matplotlib.pyplot as plt
x=[]
a=-100
while (a!=101):
    x.append(a)
    a+=1
y=[]
for i in range (len(x)):
    c=x[i]**2
    y.append(c)
plt.plot(x,y)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("Curve Graph")
plt.show()
