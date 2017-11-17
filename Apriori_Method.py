#Apriori_Method 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset= pd.read_csv('Market_Basket_Optimisation.csv',header=None)

# As input it takes list of lists so to convert table to list of list we use 2 for loop:
transactions=[] 
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for  j in range(0,20)])

#Training Apriori on dataset
from apyori import  apriori
rules=apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)  

#Visualizing our problem set's results
results=list(rules)