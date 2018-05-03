from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense
from keras.optimizers import Adam


#We need to split data into train, validation and test paths
train_path = '../dataSet/training'
valid_path = '../dataSet/validation'
test_path = '../dataSet/testing'

#Image array is (144, 256, 3)
#1034, 246 and 250 images in each directory
train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size= (144, 256), classes=['street', 'property'], batch_size=32);
validation_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size= (144,256), classes=['street', 'property'], batch_size=32);
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size= (144,256), classes=['street', 'property'], batch_size=32);

model = Sequential()
model.add(Conv2D(32, (3, 3), strides=(3, 3), activation='relu', input_shape=(144, 256, 3)))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))

model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['acc'])

model.fit_generator(train_batches, steps_per_epoch=50, validation_data=validation_batches, epochs=10, verbose=1)

# Save model and weights to folder

model.save_weights('./saved_models/test3.h5f')