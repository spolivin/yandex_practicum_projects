"""This module contains functions for analyzing music data.

The module provides functions for understanding musical data 
patterns better.
"""

__author__ = "Sergey Polivin"

import pandas as pd


def number_tracks(day: str, city: str, data: pd.DataFrame) -> int:
    """Computes day- and city-specific number of track plays.

    Given the data with users' musical preferences, returns the number
    of tracks played in a particular city on a particular day.

    Args:
        day: Name of a weekday.
        city: Name of a city.
        data: DataFrame with information on musical preferences.

    Returns:
        Integer number of track plays in a given city at a given
        time.
    """
    track_list = data[data["day"] == day]
    track_list = track_list[track_list["city"] == city]

    track_list_count = track_list["user_id"].count()

    return track_list_count


def genre_weekday(data: pd.DataFrame, day: str, time1: str, time2: str) -> pd.Series:
    """Returns a rating of 10 of the most popular music genres.

    Accumulates information about top-10 most popular genres
    on a given day at a given time.

    Args:
        data: DataFrame with information on musical preferences.
        day: Name of a weekday.
        time1: Lower bound of a time period in [hh:mm] format.
        time2: Upper bound of a time period in [hh:mm] format.

    Returns:
        pandas.Series object mapping top-10 most popular music
        genres to their corresponding track plays.
    """
    genre_df = data[data["day"] == day]
    genre_df = genre_df[genre_df["time"].between(time1, time2, inclusive="neither")]

    # Compiling a rating of the most popular genres
    genre_df_top_10 = (
        genre_df.groupby("genre")["genre"].count().sort_values(ascending=False)
    ).head(10)

    return genre_df_top_10
