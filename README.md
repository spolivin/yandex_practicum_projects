# Repository for "Data Science Specialist" Specialization (Yandex Practicum)

This is a repo of projects completed during 8-month DS/ML/NLP/CV/DL training program at "Yandex Practicum".

Each project is assigned with its own designated folder containing all related files. Due to the exclusivity of the materials provided during the course, it is forbidden to publish datasets used in the projects but, however, all *Jupyter Notebook* files which contain the solution of the projects do include all explanations as well as data processing results in the cells executed.

## Folder structure

The project folders are generally characterized by the following structure:

```
|-- [project_folder_name]
    |-- README.md
    |-- [project_name].ipynb
```
* `README.md` - *Markdown* file containing the description of the project;
* `*.ipynb` - *Jupyter Notebook* file storing the solution of the project.

## Projects

| Project name | Description | Libraries used | 
| :---------------------- | :---------------------- | :---------------------- |
| [Big Cities Music](big_cities_music) | Comparison of preferences of "Yandex.Music" users from Moscow and Saint-Peterburg depending on time of day (morning and evening) and weekday (Monday, Wednesday and Friday).| `matplotlib` `numpy` `pandas` `seaborn` `IPython`|
| [Borrowers Solvency Study](solvency_analysis) | Analysis of factors affecting the creditworthiness of clients of some bank: number of children, family status, total income and loan purpose.| `matplotlib` `numpy` `pandas` `seaborn` `IPython`|
| [Real Estate Ads Study](real_estate_eda) | Exploratory data analysis of real estate objects advertisements in Saint-Petersburg and its neighbouring localities.| `warnings` `matplotlib` `numpy` `pandas` `seaborn` `IPython`|
| [Preferred Tariff Choice](optimal_tariff) | Optimal choice of the most preferable tariff plan from the menu offered by a mobile network operator based on its users behavior patterns.| `matplotlib` `numpy` `pandas` `seaborn` `IPython` `scipy`|
| [Computer Games Market Analysis](computer_games_analysis) | Identification of profit-enhancing patterns in data and making product-oriented forecasts.| `warnings` `math` `matplotlib` `numpy` `pandas` `seaborn` `IPython` `scipy`|
| [Tariff Recommendation System](recomm_system) | Building a recommendation system that would suggest tariffs to clients of a mobile operator.| `itertools` `pprint` `typing` `matplotlib` `numpy` `pandas` `seaborn` `IPython` `sklearn`|
| [Customer Churn](churn_prediction) | Building a system capable of predicting whether a client will churn from the bank or not in the near future.| `itertools` `re` `pprint` `typing` `matplotlib` `numpy` `pandas` `seaborn` `imblearn` `IPython` `sklearn`|
| [Oil Well Location Choice](location_choice) | Building an ML model capable of determining the most optimal location for drilling a new oil well.| `typing` `matplotlib` `numpy` `pandas` `seaborn` `IPython` `sklearn`|
| [Gold Recovery Prediction[Real project]](gold_recovery) | Developing an ML model prototype for predicting recovery rate of gold from gold-bearing ore.| `functools` `typing` `matplotlib` `numpy` `pandas` `seaborn` `sklearn`|
| [Clients' Personal Data Protection](personal_data_protection) | Developing a data obfuscation algorithm such that it would make it difficult to recover personal information from it.| `typing` `matplotlib` `numpy` `pandas` `seaborn` `IPython` `sklearn`|
| [Car Prices Prediction](autos_grad_boost) | Building an optimal ML model capable of determining the prices of automobile vehicles.| `re` `sys` `time` `warnings` `pprint` `matplotlib` `numpy` `pandas` `seaborn` `catboost` `IPython` `joblib` `lightgbm` `sklearn` `xgboost`|
| [Forecasting Taxi Orders](taxi_ts_prediction) | Developing a time-series model that is capable of forecasting hourly taxi orders to the airport.| `itertools` `time` `matplotlib` `numpy` `pandas` `seaborn` `catboost` `IPython` `lightgbm` `sklearn` `statsmodels` `xgboost`|
| [Transformers-based Sentiment Analysis[GPU]](bert_toxic_comm) | Classification of commentaries into positive and toxic ones using *BERT* language model along with *GPU* support.| `time` `pprint` `typing` `matplotlib` `numpy` `pandas` `seaborn` `torch` `transformers` `catboost` `imblearn` `lightgbm` `sklearn` `tqdm` `xgboost`|
| [CV-based People's Age Determination[GPU]](resnet_age) | Building a neural net model capable of determining a person's age based on their photos.| `os` `typing` `matplotlib` `numpy` `pandas` `seaborn` `IPython` `PIL` `tensorflow.keras`|
| [Production Costs Optimization[Diploma project]](industry_temp_prediction) | Developing a prototype of an ML model that will predict a temperature of steel.| `os` `pprint` `typing` `matplotlib` `numpy` `pandas` `seaborn` `catboost` `IPython` `lightgbm` `sklearn` `xgboost`|

## Syllabus

- **Module 1**: ***Introduction to Data Analysis***

  - **Topics:** Basic Python, Data Preprocessing, Exploratory Data Analysis, Statistical Data Analysis
  - **Libraries:** `pandas` `numpy` `scipy` `matplotlib` `seaborn`

- **Module 2**: ***Basics of Machine Learning***

  - **Topics:** Introduction to Machine Learning, Supervised Learning, Machine Learning in Business
  - **Libraries:** `sklearn` `imblearn`

- **Module 3**: ***Advanced Machine Learning***
  - **Topics:** Transformers, Natural Language Processing, Gradient Boosting/Descent, Time Series, Linear Algebra
  - **Libraries:** `catboost` `lightgbm` `xgboost` `statsmodels` `re` `pymystem3` `nltk` `transformers` `torch` `tqdm`

- **Module 4**: ***Machine Learning for Big Data***
  - **Topics:** SQL (Postgres), PySpark, Unsupervised Learning, Computer Vision, Deep Learning
  -  **Libraries:** `tensorflow.keras` `pyspark` `PIL` `cv2` `pyod`
