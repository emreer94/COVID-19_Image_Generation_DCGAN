import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import os
import gdown


from google.colab import drive
drive.mount('/content/drive')
path="/content/drive/MyDrive/covidpos_dataset"