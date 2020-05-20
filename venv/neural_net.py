"""
import numpy as np
import matplotlib as plt
import tensorflow as tf
from tensorflow import keras
"""
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

df = pd.read_csv('data.csv')
data_set = df.values
x = data_set[:, 2:6]
y = data_set[:, 1]

x_train, x_val_and_test, y_train, y_val_and_test = train_test_split(x, y, test_size=.3)
x_val, x_test, y_val, y_test = train_test_split(x_val_and_test, y_val_and_test, test_size=0.5)

model = Sequential(
    [Dense(32, activation='relu', input_shape=(5,)),
     Dense(32, activation='relu'),
     Dense(1, activation='sigmoid')])

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
