# Car Prices Prediction

The service which engages in selling used cars is developing an application to attract new customers. The application enables quickly finding out the market value of the car. We have access to historical data: technical characteristics, configuration and prices of cars. The task is to build an optimal model for determining the cost of the car.

During carrying out this task, it is important to take into account the following important factors for the customer:

* Accuracy of prediction;
* Speed of prediction;
* Training time.

## Objectives

1. Developing the most optimal model for predicting the vehicle price.
2. Attaining the values of the *RMSE* metric not higher than 2,500.

## Project progress

Despite the provided access to the data, we do not know anything about the quality of the data, which will require an overview of the data and subsequent preprocessing. Furthermore, after the final preparation of data for machine learning algorithms, a number of models will be trained in order to select the optimal combination of hyperparameters, according to the results of which the best model that meets all the necessary requirements of the customer will be selected. At the last stage, the selected model will be tested on a test set.

Thus, the results of the work will be obtained during the following stages:

1. Data preprocessing and preparation.
2. Training ML models and hyperparameter tuning.
3. Models analysis.
4. Feature importances analysis and testing.

## Machine learning models 

1. **DecisionTreeRegressor**
2. **RandomForestRegressor**
3. **CatBoostRegressor**
4. **XGBRegressor**
5. **LGBMRegressor**

## Note

After running the code in `autos_price_boost.ipynb`, a file `final_model_trained.joblib` will be created and saved in the working directory. The file contains the chosen most optimal model that has already been trained. The model can thus already be used for prediction.
