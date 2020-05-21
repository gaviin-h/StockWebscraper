"""
import matplotlib as plt
import tensorflow as tf
from tensorflow import keras
"""
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
data_set = df.values
x = data_set[:, 2:6]
y = data_set[:, 1]

x_train, x_val_and_test, y_train, y_val_and_test = train_test_split(x, y, test_size=.3)
x_val, x_test, y_val, y_test = train_test_split(x_val_and_test, y_val_and_test, test_size=0.5)

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = np.reshape(y_test, (y_test.shape[0], 1))

model = Sequential([
     LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)),
     LSTM(50, return_sequences=True),
     LSTM(50, return_sequences=False),
     Dense(1)])

model.compile(optimizer='adam', loss='mean_squared_error')

hist = model.fit(x_train, y_train, batch_size=32, epochs=1000)

predicted_change = model.predict(x_test)

data = open('data.txt', 'w')
j = 0
for i in predicted_change:
    data.writelines(str(i) + ", " + str(y_test[j][0]) + "\n")
    j += 1
data.close()
