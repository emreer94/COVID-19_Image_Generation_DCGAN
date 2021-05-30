# COVID-19_Image_Generation

COVID-19 Chest X-Ray Image Generation using DCGAN

Author: emreer94

Date created: 2021/05/08

Description: DCGAN trained using fit() by overriding train_step on COVID-19 images

You can find the whole COVID-19 CXR dataset in "COVID-19 Chest X-ray Database" created by Tawsifur Rahman, Dr. Muhammad Chowdhury and Amith Khandakar.


![image](https://user-images.githubusercontent.com/17491047/120104034-30369400-c15b-11eb-9e3f-e3aa83e4baee.png)

To augment the data please select the "COVID" file (123 MB) only under "COVID-19_Radiography_Dataset" file. The directory must contain only 1 file to augment the images.


![image](https://user-images.githubusercontent.com/17491047/120104062-5eb46f00-c15b-11eb-9945-2e13beacccf7.png)

You can use this link to get the dataset: https://www.kaggle.com/tawsifurrahman/covid19-radiography-database

After rearranging the dataset directory, it is possible to adjust the input image and batch size. 
Be careful that increasing the input image size more than 128x128 causes problems in Google Colab free version for this DCGAN implementation. 
If you have any external GPU, feel free to change the given parameters or even layer activations. 


The results will go better with increasing number of epoch, you can find some sample generated images in the figure below, in 30 epochs.

![image](https://user-images.githubusercontent.com/17491047/120104323-9243c900-c15c-11eb-895f-51e981ee61bb.png)


Thank you!
