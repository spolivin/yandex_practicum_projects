# Big Cities Music

The comparison of Moscow and St. Petersburg is surrounded by myths. For example:
 * Moscow is a megapolis subject to the rigid rhythm of the working week;
 * St. Petersburg is a cultural capital, with its own tastes.

Based on "Yandex.Music" data, we will compare the behavior of users of the two capitals.

## Objective

Testing three hypotheses:

1. User activity depends on the day of the week. Moreover, in Moscow and St. Petersburg, this manifests itself in different ways.
2. On Monday morning, some genres prevail in Moscow, and others in St. Petersburg. Similarly, on Friday evening, different genres prevail — depending on the city. 
3. Moscow and St. Petersburg prefer different genres of music. In Moscow, pop music is more often listened to, in St. Petersburg - Russian rap.

## Project progress

We will get data on user behavior from `yandex_music_project.csv`. Nothing is known about the quality of the data. Therefore, an inspection of the data will be needed before testing hypotheses. 

We will check the data for errors and evaluate their impact on the study. Then, at the preprocessing stage, we will look for ways to correct the most critical data errors.
 
Thus, the study will take place in three stages:

 1. Data overview.
 2. Data preprocessing.
 3. Hypothesis testing.

## Data

The analysis is based on the following data on track plays in "Yandex.Music" service:

- Track name
- Artist
- Genre
- City
- Day of track play
- Time of track play

## Libraries

*pandas*
