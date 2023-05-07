# Customer Churn

Analysts of "Beta Bank" found out that the bank began to lose customers. This happens every month, and even though the number of customers who have left is small, such a tendency is quite noticeable. Bank marketers have found that it would be actually cheaper to retain current customers rather than attract new ones. 

The task is to predict whether the client will leave the bank in the near future or not. Historical data on customer behavior and termination of contracts with the bank are available. It is necessary to build a model with a value of *F1* metric of at least 0.59, at the same time paying attention to the values of *AUC-ROC* metric.

## Objectives

1. Building an automated system capable of analyzing bank clients behavior and predicting customer churn.
2. Attaining *F1* score of at least 0.59. 

## Project progress

Data on the behavior of "Beta Bank" customers is stored in `Churn.csv` file. At the moment, nothing is known about the quality of the data provided, which will require a detailed analysis of the data and its subsequent preprocessing (if necessary). 

The data will be checked for errors and inconsistencies. If necessary, data preprocessing will be carried out. Next, the data will be prepared for their use in machine learning algorithms. In the following sections, we will explore the aspect of classes imbalance and build several models in order to select the optimal combination of hyperparameters for various methods when both ignoring class imbalance and combating it. At the last stage, we will test the final model.

Thus, exploring and modeling of the behavior of the bank's customers will be carried out during the following stages:

1. Data preparation (overview, preprocessing, splitting, encoding, scaling).
2. Ignoring classes imbalance.
3. Accounting for classes imbalance (weighting, upsampling, downsampling).
4. Final model selection and testing.
5. Sanity check.

## Machine learning models 

1. **Decision Tree**
2. **Random Forest**
3. **Logistic Regression**

## Data 

[https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)

## Libraries

`sklearn` `imblearn` `numpy` `pandas` `matplotlib` `seaborn` `re`
