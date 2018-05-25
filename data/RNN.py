import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

limit=100
features = open('time_features.txt', 'r').read().split()[0:limit]
labels = open('time_labels.txt', 'r').read().split()[0:limit]

def create_dataset(dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-look_back-1):
                a = dataset[i:i+look_back]
                dataX.append(a)
                dataY.append(dataset[i + look_back])
        return numpy.array(dataX), numpy.array(dataY)

look_back = 1
trainX, trainY = create_dataset(features, look_back)
testX, testY = create_dataset(labels, look_back)

trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=1, validation_split=.1)

model.save('time_predictor.h5')
