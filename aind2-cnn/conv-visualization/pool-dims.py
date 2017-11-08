from keras.models import Sequential
from keras.layers import MaxPooling2D

model = Sequential()
model.add(MaxPooling2D(pool_size=3, strides=2, padding='same', input_shape=(100, 100, 15)))
model.summary()