# Clients' Personal Data Protection

The customer is a company engaged in insurance. The task set is to develop a method of data transformation, after which it would be challenging to recover personal information. An important condition for creating such an algorithm is that the quality of machine learning models should not deteriorate.

## Objectives

1. Development of an algorithm for protecting customers' personal data.
2. Achieving close values of *R2* metric of machine learning models before and after data transformation.

## Project progress

We have been granted access to the insurance company's customer data containing various attributes. Nothing is known about the quality of the data, which will require a data overview. Next, we will analyze the question regarding the effect of multiplication of features by an invertible matrix on the values of the quality metric of the model. At the final stage, an algorithm will be proposed that will provide reliable protection of personal data.

Thus, the results of the study will be obtained as a result of completing the following steps:

1. Loading data.
2. Data overview.
3. Matrix multiplication analysis.
4. Suggesting and programming data protection algorithm.

## Machine learning models 

1. **LinearRegression**

## Data 

The data is contained in the `insurance.csv` file. The characteristics of clients include the gender, age and salary of the insured persons, as well as the number of their family members. The target feature will be the number of insurance payments to the client over the past 5 years.

## Libraries

`sklearn` `numpy` `pandas` `matplotlib` `seaborn`
