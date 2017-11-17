import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset= pd.read_csv('Data.csv')
x=dataset.iloc[:, :-1].values
y=dataset.iloc[:,3].values

#Missing data handling
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(x[:,1:3])              
x[:,1:3]=imputer.transform(x[:,1:3])


#Encoding categorial data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder_x=LabelEncoder()
x[:, 0]=labelEncoder_x.fit_transform(x[:,0])
onehotencoder= OneHotEncoder(categorical_features = [0])
x=onehotencoder.fit_transform(x).toarray()
labelencoder_y=LabelEncoder()
y=labelEncoder_x.fit_transform(y)


#Spiltting the dataset and training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state=42)

#feature Scaling 
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

