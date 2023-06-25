# Production Costs Optimization[Diploma project]

Steel works is in the process of finding ways to optimize its production costs. One of the sources for achieving this goal is electricity, the consumption of which the plant wants to reduce during the steel processing stage. The task is to develop a prototype of a model capable of predicting the temperature of steel with good accuracy.

## Objectives

1. Optimization of production by reducing the amount of electricity consumed.
2. Building a predictive model for determining the steel temperature.
3. Achieving the target values of the quality metric.

## Project progress

In order to achieve the goals of the project, we have been given access to extensive information from various steel processing stages. Nothing is known about the quality of the data, which will require a primary analysis of the data as well as a subsequent exploratory analysis of the data, as a result of which we can become more familiar with the features of the data.

After identifying problems with the data, we can use the appropriate data analysis tools to preprocess them. After fixing the problems, we will move on to the next stage of data preparation, during which the data will be divided into training and test sets. Additionally, we can build a number of pipelines to simplify preprocessing and enable us to do preprocessing at the time of model training.

The next step is modeling, where we will use the selected machine learning/gradient boosting algorithms and fine-tune them through cross-validated grid search. Based on the results of the selection of hyperparameters, the best model will be identified and further tested on a new data set.

Thus, the results of the project will be achieved in the process of the completion of the following steps:

1. Primary data analysis.
2. Exploratory data analysis.
3. Data preprocessing.
4. Data preparation.
5. Grid search and cross-validation.
6. Feature importances analysis.
7. Model testing and adequacy check.

## Machine learning models 

1. **LinearRegression**
2. **DecisionTreeRegressor**
3. **RandomForestRegressor**
4. **Ridge**
5. **LASSO**
6. **CatBoostRegressor**
7. **XGBRegressor**
8. **LGBMRegressor**
