# Forecasting Taxi Orders

The client is a company engaged in the transportation of passengers by taxi. The company collected historical data on taxi orders at airports to determine peak periods to attract more drivers at such times. The task is to build a model that could predict the number of taxi orders for the next hour in such a way that the value of the metric *RMSE* in the test set would not be greater than 48.

## Objectives

1. Building a model for predicting the number of taxi orders.
2. Achieving the value of the metric *RMSE* no more than 48.

## Project progress

We have been given access to historical data on taxi orders, but it is not yet clear of what quality they are and whether pre-processing will be required. This will be checked, after which we will resample the data and get to data analysis. Furthermore, the data will be prepared and subsequently used in the process of training and tuning different machine learning models. Based on the results of the selection of hyperparameters, the best model will be selected, which will be then tested. 

Thus, the results will be obtained during the following steps:

1. Loading data.
2. Data analysis.
3. Data preparation.
4. Selection of hyperparameters.
5. Model analysis.
6. Testing.

## Machine learning models 

1. **DecisionTreeRegressor**
2. **RandomForestRegressor**
3. **CatBoostRegressor**
4. **XGBRegressor**
5. **LGBMRegressor**


## Libraries

*sklearn*

*catboost*

*xgboost*

*lightgbm*

*numpy*

*pandas*

*matplotlib*

*seaborn*

*statsmodels*

*itertools*
