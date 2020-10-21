import seaborn as sns
import pandas as pd
from matplotlib.pyplot import *

sns.set_theme()

dat = pd.read_csv("rainYearly.csv")

tem=pd.read_csv("tempYearly.csv")

dat["Temperature"]=tem["Temperature"]

sns.regplot(x="Rainfall", y="Temperature", data=dat)
    
show()
