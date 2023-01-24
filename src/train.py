# coding: utf-8

import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression


# чтение и подготовка данных
df = pd.read_csv('heart_cleveland_upload.csv')

y=df.copy()['condition']
x=df.copy().drop('condition',axis=1)


# обучение модели
model = LogisticRegression()
model.fit(x,y)

# сохранение модели
pickle.dump(model,open('model.save','wb'))

