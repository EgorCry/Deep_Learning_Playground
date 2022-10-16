import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense, GRU
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler


def create_model():
    model = Sequential(name='Temperature')
    model.add(GRU(50, input_shape=(1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


with open('01') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()

n = int(data[0])
margin = n
train = np.array([float(i) for i in data[1:margin]])
m = int(data[margin+1])
test = [float(i) for i in data[margin+2:]]

scaler = MinMaxScaler()
train = scaler.fit_transform(train)
test = scaler.transform(test)

model = create_model()
split = int(0.75 * train)
model.fit(train[:split], train[split:], epochs=100)
print(model.predict(train.reshape(len(train), 1, 1)), test[-1])
