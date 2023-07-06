# Real Estate Ads Study

We have the data provided by "Yandex Real Estate" service - archive of real estate objects advertisements in St. Petersburg and neighbouring localities for several years. It is necessary to understand how to accurately determine a market value of real estate objects. The objective is to set the parameters. This will allow building an automated system: it will track anomalies and detect fraudulent activity.

Each real estate object is characterized by two types of features: 

* Those specified by a user.
* Those automatically retrieved based on cartographic data (for instance, distance to city center, airport, park or reservoir).

## Objectives

1. Determining a market value of real estate objects.
2. Building an automated system that will track anomalies and detect fraudulent activities.
3. Identifying the main determinants of real estate prices.

## Project progress

Nothing is known about the quality of data provided. Thus, we will need to conduct data preprocessing to check for potential inconveniences, inaccuracies and anomalies.

Data will be verified for errors and evaluated. Then, at the preprocessing stage, we will look for a way to correct errors in data which will not result in data distortions. Then, additional necessary columns will be created and we will get to exploratory data analysis (EDA).

Thus, the study will be conducted in six stages:

1. Data overview.
2. Data Preprocessing.
3. Calculations and adding results to the table.
4. EDA for neighboring localities.
5. EDA for St. Petersburg.
6. Price factors analysis.

## Data

The analysis is based on the following data on real estate objects:

- Price
- Total area
- Kitchen area
- Living area
- Number of rooms
- Ceiling height
- Number of floors in a building
- Floor of an object
- Balconies
- Locality names
- Distances to the city center, nearest airport, park, reservoir
- Numbers of parks, ponds within a 3-kilometer radius
- Number of photos in the ad
- Publication date
- Duration of ad placement
