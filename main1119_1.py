import os
import tensorflow as tf
from PIL import Image
from tensorflow import keras
import numpy as np

all_files = []
for i in range(0,10):
    path_dir = './images/training/{0}'.format(i)
    file_list = os.listdir(path_dir)
    file_list.sort()
    all_files.append(file_list)

train_images = []
train_labels = []
for num in range(0,10):
    for numbers in all_files[num]:
        img_path = './images/training/{0}/{1}'.format(num,numbers)
        print("load :"+img_path)
        img = Image.open(img_path)
        train_images.append(np.array(img))
        train_labels.append(num)

eval_files = []
for i in range(0,10):
    path_dir = './images/training/{0}'.format(i)
    file_list = os.listdir(path_dir)
    file_list.sort()
    eval_files.append(file_list)

test_images = []
test_labels = []
for num in range(0,10):
    for numbers in eval_files[num]:
        img_path = './images/training/{0}/{1}'.format(num,numbers)
        print("load :"+img_path)
        img = Image.open(img_path)
        test_images.append(np.array(img))
        test_labels.append(num)

train_images = train_images.reshape((60000,28,28,1))
test_images = test_images.reshape((10000,28,28,1))

train_images, test_images = train_images / 255.0, test_images / 255.0

model = keras.Sequential()
model.add(keras.layers.Conv2D(32,(3,3), activation='relu', input_shape=(28,28,1)))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Conv2D(64,(3,3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Conv2D(64,(3,3), activation='relu'))

model.summary()

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(10, activation="softmax"))
model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images,train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(test_acc)