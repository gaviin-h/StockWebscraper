import numpy as np
import pandas as pd
import matplotlib as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

mushroom_df = pd.read_csv('data.csv')
mushroom_df.head(28)
mushroom_df.describe()
