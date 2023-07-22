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

## Final model

The final model that proved to be better than others under consideration is as follows:

```
{'standardscaler': StandardScaler(),
 'xgbregressor': XGBRegressor(base_score=None, booster=None, callbacks=None,
              colsample_bylevel=None, colsample_bynode=None,
              colsample_bytree=None, early_stopping_rounds=None,
              enable_categorical=False, eval_metric=None, feature_types=None,
              gamma=None, gpu_id=None, grow_policy=None, importance_type=None,
              interaction_constraints=None, learning_rate=0.13, max_bin=None,
              max_cat_threshold=None, max_cat_to_onehot=None,
              max_delta_step=None, max_depth=4, max_leaves=None,
              min_child_weight=None, missing=nan, monotone_constraints=None,
              n_estimators=60, n_jobs=None, num_parallel_tree=None,
              predictor=None, random_state=None, ...)}
```

In other words, the winning model is the gradient boost model from `xgboost` library with parameters specified above. It should be noted that since the model here basically represents a pipeline, the data are first scaled and then get fed into the model.

We have managed to attain the following key metric score (*Mean Absolute Error*):

```
mae_test = 6.661
```

Were were able to achieve the required quality requirements and in this case the model predicts the final temperature with an error of about 6.6 degrees on average.

## Training features

The following features have been used when training the best model and generating predictions:

1. `init_temp`
2. `energy`
3. `gas_1`
4. `bulk_1`
5. `bulk_2`
6. `bulk_3`
7. `bulk_4`
8. `bulk_5`
9. `bulk_6`
10. `bulk_7`
11. `bulk_8`
12. `bulk_10`
13. `bulk_11`
14. `bulk_13`
15. `bulk_15`
16. `wire_2`
17. `wire_3`
18. `wire_4`
19. `wire_6`
20. `wire_7`
21. `wire_8`
22. `wire_9`

In total the training process included 22 features which have been used for final model selection and subsequent testing. Notably, there are features that have already been present in the datasets as well as features we have managed to additionally create.

## Hyperparameters

The best model is a Gradient Boosting model from `xgboost` library with the following optimally chosen hyperparameters:

```
{'xgbregressor__n_estimators': 60,
 'xgbregressor__max_depth': 4,
 'xgbregressor__learning_rate': 0.13}
```

## Project improvement recommendations

As far as the recommendations for improving the model are concerned, the following points should be noted:

1. It would be possible to try to exclude from the model the factors with the smallest scores in accordance with the calculated feature importances. The metric will not change much, but we will get rid of factors whose effects are not statistically significant.
    
2. We could try to experiment further with the values of hyperparameters when searching through the grid. We can probably find better combinations. We can immediately increase the number of iterations of `n_iter` for `RandomizedSearchCV`.
    
3. Since we are dealing with multicollinearity, we could also try lots of other models here, including neural networks (for example, `MLPRegressor` from `sklearn`).
    
4. As mentioned earlier, we could check the data for adequacy using dates, which would probably remove some low-quality ladles.
    
