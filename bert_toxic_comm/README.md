# Transformers-based Sentiment Analysis[GPU]

Online store "Wikiship" launches a new service. Users are now given the opportunity to independently edit and supplement product descriptions, as is the case in wiki-communities. In other words, customers can offer their own edits and comment on the changes of others. The store needs a tool that will search for toxic comments and send them for moderation. The objective is to develop and train a model to classify comments into positive and negative ones so that the value of *F1* metric would be higher than 0.75. We have at our disposal a set of data marked up by the toxicity of edits.

## Objectives

1. Developing an automated system of determining the degree of toxicity of comments.
2. Achieving the value of the *F1* metric of at least 0.75.

## Project progress

The data provided will be downloaded and studied. Since machine learning models cannot work with text data in its original form, we will have to encode it. This will be done using *BERT* language model (*Bidirectional Encode Presentations from Transformers*), which will imply features creation by a means of embeddings that will be further used in the process of modeling and selection of the optimal model.

Thus, the goals of the project will be realized as a result of the following steps:

1. Loading data.
2. Data preparation.
3. Models training and selection of hyperparameters.
4. Models analysis.
5. Testing and quality/sanity check.
6. Analysis of the final model.

## Transformer models (Hugging Face)

1. `unitary/toxic-bert`
2. `martin-ha/toxic-comment-model`

## Machine learning models 

1. **DecisionTreeRegressor**
2. **RandomForestRegressor**
3. **KNeighborsClassifier**
4. **CatBoostRegressor**
5. **XGBRegressor**
6. **LGBMRegressor**

## Note

The project was carried out using *BERT* neural net, the creation of embeddings with which is a computationally expensive process in terms of the number of calculations that need to be performed per unit of time. Therefore, for the fastest code execution, it is recommended to use *GPU* (for example, free, but limited, *GPU* on the [Google Colab](https://colab.research.google.com/)). The code was written in such a way so that running the code on both *CPU* and *GPU* would be possible.

## Libraries

`torch`

`transfomers`

`tqdm`

`sklearn`

`imblearn`

`catboost`

`xgboost`

`lightgbm`

`numpy`

`pandas`

`matplotlib`

`seaborn`
