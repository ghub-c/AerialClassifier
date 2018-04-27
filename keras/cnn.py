from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense
from keras.optimizers import Adam

'''
img = load_img('../dataSet/training/street/1vuelo (72).png')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
print(x.shape)
'''
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
model.add(Flatten()),
model.add(Dense(2, activation='softmax'))

model.compile(Adam(lr=.0001), loss='mean_squared_error', metrics=['acc'])

model.fit_generator(train_batches, steps_per_epoch=50, validation_data=validation_batches, epochs=10, verbose=1)
