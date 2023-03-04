# Gold Recovery Prediction[Real project]

The company that provided the project engages in developing solutions to achieve the efficiency of industrial enterprises. As data scientists, we have been tasked with preparing a prototype of a machine learning model that will have to predict the recovery coefficient of gold from gold-bearing ore using data on the parameters of extraction and purification. The model will help to optimize production so as not to launch an enterprise with unprofitable characteristics.

## Objectives

1. Developing the most optimal model for predicting gold recovery rate.
2. Achieving the lowest values of the *sMAPE* metric.
3. Optimization of production by avoiding its launch in a loss-making state.

## Project progress

In order to complete the project, an access to raw data is provided, the quality of which is unknown, which will require data validation for correctness and their subsequent preprocessing (if necessary). As soon as the data has been prepared, an exploratory data analysis will be necessary for a deeper understanding of the data provided. Next, a number of regression machine learning models will be trained, from which, based on cross-validation and the values of the target metric *sMAPE*, the best one will be selected and later tested.

Thus, the results of the study will be obtained as a result of completing the following steps:

1. Loading and preparing data.
2. Exploratory data analysis.
3. Training and validating ML models.
4. Testing the final model.

## Data 

Data provided for the project are stored in the following three `csv`-files: 

* `gold_recovery_train_new.csv` => Training data.
* `gold_recovery_test_new.csv` => Testing data.
* `gold_recovery_full_new.csv` => Full data.

## Machine learning models 

1. **LinearRegression**
2. **DecisionTreeRegressor**
3. **RandomForestRegressor**

## Note

The data are indexed by the date and time of obtaining the information (`date` feature), as a result of which the neighboring parameters are often similar. Some parameters are not available because they are measured and/or calculated much later. Because of this, some features that may be in the training set are missing in the test set. Besides, there are no target features in the test set.

## Libraries

*sklearn*

*numpy*

*pandas*

*matplotlib*

*seaborn*
