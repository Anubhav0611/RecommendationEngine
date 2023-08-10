import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
df =pd.read_csv('Dataset.csv')
x = df.iloc[:,3:5].values
y = df.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.ensemble import RandomForestRegressor
regressor_rf=RandomForestRegressor(random_state=0)
regressor_rf.fit(x_train,y_train)
y_pred_rf= regressor_rf.predict(x_test)

print (regressor_rf.predict([[1.1753125,1.814288]]))
#pickle.dump(regressor_rf,open('Combined_Score_Model.pkl', 'wb'))