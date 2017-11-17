#Polynomial Regression

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
"""                
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
sc_y = StandardScaler()"""
#linear model
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

#polynomial model creation
from sklearn.preprocessing import PolynomialFeatures
pol_reg=PolynomialFeatures(degree=4)  #Degree is x,x1,x2,x3,......
x_poly=pol_reg.fit_transform(x)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

#Visualization of our linear regression
import  matplotlib.pyplot as plt
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title("TRUTH AND BLUFF OF SALARY BASED ON LEVEL with LINEAR REGRESSION")
plt.xlabel("POSITION LEVEL")
plt.ylabel("SALARY")
plt.show()

#Visualization of polynomial regressor
import  matplotlib.pyplot as plt
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(x_poly),color='blue')
plt.title("TRUTH AND BLUFF OF SALARY BASED ON LEVEL with POLYNOMIAL REGREESION")
plt.xlabel("POSITION LEVEL")
plt.ylabel("SALARY")
plt.show()

#x_grid to make more correct prediction with smaller step size so we can avoid linear feature with 1-2 , 2-3,....9-10
x_grid=np.arange(min(x),max(x),0.1)
x_grid=x_grid.reshape((len(x_grid)),1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_reg2.predict(pol_reg.fit_transform(x_grid)),color='blue')
plt.title("TRUTH AND BLUFF OF SALARY BASED ON LEVEL with POLYNOMIAL REGREESION")
plt.xlabel("POSITION LEVEL")
plt.ylabel("SALARY")
plt.show()

#predict new value with linear regression
lin_reg.predict(6.5)

#predict new value with polynomial regression
lin_reg2.predict(6.5)