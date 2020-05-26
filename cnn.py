#from matplotlib import pyplot
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from math import ceil
(trainX, trainY), (testX, testY) = mnist.load_data()
trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))[:10000]
testX = testX.reshape((testX.shape[0], 28, 28, 1))[:2000]
trainY = to_categorical(trainY)[:10000]
testY = to_categorical(testY)[:2000]

train_norm = trainX.astype('float32')
test_norm = testX.astype('float32')
train_norm = train_norm / 255.0
test_norm = test_norm / 255.0
trainX,testX=train_norm,test_norm

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(trainX, trainY, epochs=10,validation_data=(testX, testY))

_,acc=model.evaluate(testX,testY)

with open("/task/accuracy.txt",'w') as f:
    f.write(str(ceil(100*acc)))
