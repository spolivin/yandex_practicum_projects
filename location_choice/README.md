# Oil Well Location Choice

The mining company "Glavneft" is planning to start drilling a new well. As analysts of the company, our goal is to determine the most optimal place for the implementation of such an initiative.

We have been provided with data on oil wells in 3 regions, where the quality of oil and the volume of reserves have been measured for all of their 100,000 oil wells in each region. It is necessary to build a machine learning model that will help to determine the region where mining will bring the greatest profits, as well as analyze possible profits and risks with the *Bootstrap* technique.

When choosing a location, the following algorithm of actions is usually used:

* Searching for oil wells reserves in the selected region, where values of features are calculated for each oil well;
* Building a model and estimating the volume of oil reserves;
* Selection of the oil wells with the highest estimates of oil reserves, where the number of oil wells depends on the company's budget and the cost of developing one well;
* Calculation of profit equal to the total profit of the selected oil wells.

## Objectives

1. Building a model to determine the most optimal region for drilling a new well.
2. Conducting a statistical analysis of profits and risks using the *Bootstrap* technique.

## Project progress

Data on geological exploration in the presented regions will be uploaded and checked for errors and inconsistencies, as a result of which, if necessary, data preprocessing will be carried out. Next, the final preparation of the data for their use in machine learning algorithms will be carried out. The prepared data will then be used in the process of training the model and calculating predictions. The results obtained will be further used to calculate the profit for the regions. At the last stage, an analysis of risks and profits for each region will be performed using statistical data analysis tools.

Thus, the results of the study will be obtained as a result of completing the following steps:

1. Loading and preparing data.
2. Training and validating the model.
3. Preparation for profit calculation.
4. Calculation of profit and risks.

## Machine learning models 

1. **LinearRegression**

## Data 

The exploration data is contained in three *csv*-files for each of the three regions, respectively:

* `geo_data_0.csv` => **Region #1**
* `geo_data_1.csv` => **Region #2**
* `geo_data_2.csv` => **Region #3**

## Libraries

`sklearn` `numpy` `pandas` `matplotlib` `seaborn`
