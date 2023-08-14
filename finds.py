import pandas as pd
import numpy as np
data=pd.read_csv("enjoysport.csv")
print(data)
d=np.array(data)[:,:,-1]
print(d)
target=np.array(data)[:,-1]
def train(c,t):
    for i , val in enumerate(t):
        specific_hypothesis=c[i].copy()
        break
    for i , val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis = '?'
                else:
                    pass

print("The final hypothesis is: ",train(d,target))
