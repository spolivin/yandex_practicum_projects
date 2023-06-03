# CV-based People's Age Determination[GPU]

The customer is the chain supermarket which intends to implement a system of computer vision for processing photos of customers. Photo fixation in the checkout area will help to determine the age of customers in order to:

* Analyze purchases and offer products that may be of interest to buyers of this age group;
* Monitor the integrity of cashiers when selling alcohol.

The task is to build a model which determine an approximate age of a person given the data of people's images with their respective ages. It is important that the value of *Mean Absolute Error* not exceed 8.

## Objectives

1. Developing a neural network capable of determining ages of customers.
2. Attaining *MAE* score of less than 8. 

## Project progress

The image dataset along with labels with ages will be uploaded and analyzed. Afterwards, the data will be appropriately prepared for deep learning algorithms. The model will be trained on *GPU* server provided by *Yandex Practicum*.

Thus, exploring and modeling supermarket customers' ages using images will be carried out during the following stages:

1. Exploratory data analysis.
2. Data preprocessing and preparation.
3. Training the neural network.
4. Analysis of the results.

## Data 

The dataset which has been used for training the neural network was taken from [ChaLearn Looking at People](http://chalearnlap.cvc.uab.es/dataset/26/description/).

The data has been uploaded from Kaggle:
[https://www.kaggle.com/datasets/abhikjha/appa-real-face-cropped](https://www.kaggle.com/datasets/abhikjha/appa-real-face-cropped)
