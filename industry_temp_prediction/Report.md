# Report

## Project progress analysis

This study was devoted to building a model for predicting the final temperature of steel pouring. We were able to sequentially go through all the necessary stages of data analysis and create a model that not only has the required quality, but also meets the adequacy criteria.

In particular, the analysis included the following components:

1. Primary data analysis.
2. Exploratory data analysis.
3. Data processing.
4. Creating features and combining data.
5. Analysis of multicollinearity.
6. Modeling.
7. Model testing.

As part of this study, all the points of the plan were successfully completed, as a result of which we were able to properly process the data and then use them to build a prototype of the most optimal model. It should be noted that another method of testing the data for adequacy was not used in the work, namely, the time comparison of the time of adding additives to the ladle with the time of temperature measurements. It is likely that in the process of considering this possibility, we could identify a number of ladles that have some timing inconsistencies.

## Analysis of the main project difficulties

Regarding the main difficulties encountered in the process of implementation of this project assignment, one may highlight, first of all, the presence of a large number of missing values in the data. However, nevertheless, armed with knowledge of the nature of the data, it was possible to successfully deal with this problem. Secondly, having a certain number of outliers in the data would make it much more difficult to find the optimal model, but fortunately, knowing the logical and realistic ranges of values in the data, we were able to quickly deal with the problem of outliers.

Furthermore, no less interesting problem was the combination of DataFrames into one final table for modeling. Having singled out the target variable, as well as features (both engineered and already included), the question arose as to how exactly the data should be merged. On the one hand, joining data by `left` would include all ladles and all available information (which remains after data preprocessing) in the final table, but this would again create missing values problem in the data. On the other hand, merging DataFrames by `inner` would include only those ladles that are present in the data without any gaps (after all, they have already been preprocessed for all ladles). For modeling, it was the `inner` method of combining that was chosen, because we already have a sufficient number of objects in the data, which we can also have in one place without any gaps and without the need to fill them (and therefore, synthetically distort the data).

Fourthly, the presence of multicollinearity in the data also created certain problems, because ignoring this problem would lead not only to inaccurate and inconsistent results of building a regression model, but also to a decrease in the speed of calculations. This problem was solved with the help of correlation matrices heatmaps, which helped us to get rid of other regressors and reduce the degree of multicollinearity between independent variables.

Perhaps, the last and the main problem that arose during the implementation of the project was to achieve the required level of model quality, expressed by the *MAE* metric at 6.8 degrees. In the first version of the search for optimal models using *grid search*, it was not possible to achieve the required level of quality, which always varied within the approximate range of 6.80-7.02. The problem was solved by redefining the values of variable hyperparameters, as well as increasing the number of `n_iter` combinations selected by the `RandomizedSearchCV` algorithm from 5 to 15. In the case of hyperparameters, we, in particular, reduced the number of trees, as well as their depth, which led to a slightly higher degree of the *generalization power*. By increasing the number of iterations, we simply increased the number of paths to consider and, as a result, we were able to find the optimal combination of hyperparameters.

## Key steps of the project assignment

Among the most important steps that were used in the process of carrying out this study, I would like to highlight the following:

1. **Exploratory data analysis**. This stage helped to get acquainted with the data and get the necessary insights that tabular data cannot always provide. Numbers are also a great source of information but the human eye perceives pictures and graphs better than numbers.

2. **Data processing and features engineering**. Within this stage, we were able to remove redundant information and add additional information to the data, which ultimately led to a satisfactory performance of the model, which can be seen in *features importances*.

3. **Combining data and grid search**. These steps were necessary to optimize the model.

In a nutshell, we can say that all stages of the work were viable, because each step carried a certain logic and utility, without which we would not have been able to find the optimal model with the appropriate quality.
