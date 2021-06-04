#Dataset formed containing 3615 COVID-19 CXR images and resize to 128x128
dataset = keras.preprocessing.image_dataset_from_directory(
    path, label_mode=None, image_size=(128, 128), batch_size=32
)
dataset = dataset.map(lambda x: x / 255.0) #Create the dataset and rescale the images to [0-1] range

#Display a sample image
for x in dataset:
    plt.axis("off")
    plt.imshow((x.numpy() * 255).astype("int32")[0])
    print(x.shape)
    break