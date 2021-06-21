from typing import Counter
from numpy import mod
import pandas as pd
from collections import Counter as Cn

from pandas.core.algorithms import mode

data = pd.read_csv("SOCR-HeightWeight.csv")
height = data["Height(Inches)"].tolist()
test = [1,2,3,1,1,3,1,1,3,1]
data1 = Cn(height)


moderange = {"61-65":0,"66-70":0,"71-75":0}
for key,value in data1.items():
    if 61 < float(key) < 65:
        moderange["61-65"] = moderange["61-65"] + 1
    elif 66 < float(key) < 70:
        moderange["66-70"] = moderange["66-70"] + 1
    elif 71 < float(key) < 75:
        moderange["71-75"] = moderange["71-75"] + 1


moderange1,modeoccurance = 0,0

for key,value in moderange.items():
    if value > modeoccurance:
        moderange1,modeoccurance = [int(key.split("-")[0]), int(key.split("-")[1])], value

mode = moderange1

finalmode  = (mode[0] + mode[1])/2

print(finalmode)


