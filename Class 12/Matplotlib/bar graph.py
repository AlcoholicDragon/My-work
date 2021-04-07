import matplotlib.pyplot as plt
import numpy as np

x=np.arange(4)
y=[[5.,25.,45.,30.],[6.,2.4,5.6,7.8],[3.,4.,5.6,3.4],[4.,5.,6.,7.]]
plt.title("LOL")
plt.xlabel("X LOL")
plt.ylabel("Y LOL")
plt.bar(x,y[0],color="r",width=0.25,label="LOL1")
plt.bar(x+0.3,y[1],color="g",width=0.25,label="LOL2")
plt.bar(x+0.6,y[2],color="b",width=0.25,label="LOL3")

plt.legend(loc="upper right")
plt.show()
