from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator

img = load_img('../dataset/calle/1vuelo (1).png')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
print(x.shape)

#We need to split data into train, validation and test paths
train_path
valid_path
test_path

#ImageDataGenerator to generate a batch of images from directori
train_batches = ImageDataGenerator().flow_from_directory(train_path, targe_size(,), classes=[],batch_size=10);

