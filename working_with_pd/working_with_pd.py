import pandas as pd
import seaborn as sns
import pandas as pd
from matplotlib.pyplot import *
from random import *

rye=pd.read_csv("rainYearly.csv")
tye=pd.read_csv("tempYearly.csv")

#checking the data type of all entries
for i in rye:
    for j in range(len(rye[i])):
        type(rye[i][j])

#changing two random float data type entries to int
for i in range(2):
    k=randint(1,61)
    int(rye["Rainfall"][k])

#plotting a graph   
sns.set_theme()

rye["Temperature"]=tye["Temperature"]

sns.regplot(x="Rainfall", y="Temperature", data=rye)
    
show()
