# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:54:22 2017

@author: kishan
"""
import numpy as np
X = np.random.randint(2, size=(6, 100))
Y = np.array([1, 2, 3, 4, 4, 5])


for num in X[2:3]:
    print(X[num]+"\n")
    '''
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()

print(clf)


clf.fit(X, Y)

print(clf.predict(X[2:3]))
'''
