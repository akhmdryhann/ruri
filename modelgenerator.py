# -*- coding: utf-8 -*-
"""# Predict"""
import pandas as pd
import sklearn

df = pd.read_csv('scoremath.csv')

X = df.drop(['Unnamed: 0','math score'],axis=1)
y = df['math score']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train,y_train)
y_predict = regressor.predict(x_test)
y_predict

import joblib
joblib.dump(regressor, "model.pkl")