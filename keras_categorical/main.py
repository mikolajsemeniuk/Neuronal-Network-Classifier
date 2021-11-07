from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import to_categorical

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from numpy import ndarray
from pandas import DataFrame
from typing import List, Dict, Tuple, Callable, Any

iris = load_iris()
inputs: ndarray = iris.data
targets: ndarray = iris.target

inputs_train: ndarray
inputs_test: ndarray
targets_train: ndarray
targets_test: ndarray

inputs_train, inputs_test, targets_train, targets_test = \
    train_test_split(inputs, targets, test_size = 0.3, random_state = 80718)

model = Sequential()
model.add(Dense(64, input_dim = 4, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
print(model.summary())

model.fit(inputs_train, to_categorical(targets_train), epochs = 100, verbose = 1)