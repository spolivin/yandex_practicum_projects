# Tariff Recommendation System

The mobile operator "Megaline" found out that many customers use archive tariffs. They want to build a system capable of analyzing customer behavior and offering 
users a new tariff: "Smart" or "Ultra".

We have at our disposal data on the behavior of customers who have already switched to these tariffs. We will need to build a model for solving the classification 
task that will recommend the appropriate tariff to users of the company. It is important that the model should perform with *accuracy* of at least 75%.

## Objectives

1. Building a recommendation system that would offer customers tariffs.
2. Attaining *accuracy* of at least 0.75. 

## Project progress

We possess data on "Megaline" users behavior stored in `users_behavior.csv`. The data analyzed is already prepared for using it in machine learning algorithms but 
nevertheless the data will be verified for potential errors, discrepancies and omissions. Afterwards, in order to solve the classification problem, the data will be
divided into training, validation and test sets. Next, a series of hypeparameter tunings will be conducted based on three classification models chosen so as to 
select the best hyperparameters settings for each one. The selected models will be then compared between each other and the best-performing one will be chosen that 
will be tested on the test set. Lastly, the model will be checked for adequacy.

Hence, the process of building a recommendation system will consist of the following stages:

1. Data overview.
2. Division into training, validation, test sets.
3. Training models and hyperparameters tuning.
4. Model selection and testing.
5. Sanity check.

## Machine learning models 

1. **Decision Tree**
2. **Random Forest**
3. **Logistic Regression**

## Data 

* Number of calls
* Duration of calls
* Number of SMS messages
* Internet traffic used
* Indicator of a tariff

## Libraries

*pandas*

*matplotlib*

*sklearn*
