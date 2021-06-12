import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
import os
from tensorflow.keras.optimizers import RMSprop
from PIL import Image

class callBackFunc (tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = {}):
            if(logs.get('accuracy')!= None):
                if(logs.get('accuracy') > 0.998):
                    print("99.8% acc")
                    self.model.stop_training = True


train = ImageDataGenerator(rescale = 1./255)
test = ImageDataGenerator(rescale = 1./255)

train_gen = train.flow_from_directory(
    './Model/train',
    target_size = (200, 200),
    batch_size = 41, # 10 batches/ total is 980 images
    class_mode= 'binary'
)

test_gen = test.flow_from_directory(
    './Model/tests',
    target_size = (200,200),
    batch_size = 49, # 10 batches/ total is 820 images
    class_mode= 'binary'
)

model = keras.models.Sequential([
        keras.layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (200, 200, 3)),
        keras.layers.MaxPooling2D (2,2),
        keras.layers.Conv2D(16, (3,3), activation = 'relu'),
        keras.layers.MaxPooling2D (2,2),
        keras.layers.Flatten(),
        keras.layers.Dense(300, activation = 'relu'),
        keras.layers.Dense(200, activation = 'relu'),
        keras.layers.Dense(1, activation = 'sigmoid')
])

model.summary()

model.compile(
    loss = 'binary_crossentropy',
    optimizer = RMSprop(learning_rate = 0.001),
    metrics = ['accuracy']
)

model.fit(
    train_gen,
    steps_per_epoch= 20,
    epochs = 9,
    validation_data= test_gen,
    validation_steps= 20
)

model.save('ModelFile')
