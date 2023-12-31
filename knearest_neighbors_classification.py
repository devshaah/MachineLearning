# -*- coding: utf-8 -*-
"""Knearest_Neighbors_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S56b-TYOd5-IsepQXbCQygMsHEBdaoBM
"""

#checks the most no of neighbors in same class

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
df = pd.DataFrame(load_iris().data, columns= load_iris().feature_names)
df['target'] = load_iris().target

df0 = df[:50]
df1 = df[51:100]
df2 = df[100:150]

plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color='green')
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='red')
plt.scatter(df2['sepal length (cm)'],df2['sepal width (cm)'],color='yellow')

from sklearn.model_selection import train_test_split
X = df.drop(['target'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)
knn.score(X_test,y_test)

from sklearn.metrics import confusion_matrix
import seaborn as sn
y = knn.predict(X_test)
sn.heatmap(confusion_matrix(y_test, y),annot=True)