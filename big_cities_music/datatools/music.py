"""
This module provides functions for better understanding 
the behavioral patterns of "Yandex.Music" users.

Specifically, additional functions that are hereby introduced
deal with: 

* Determining the popularity of music tracks in a specific 
    city/weekday.
* Conducting genre-specific popularity analysis. 

"""

from __future__ import division, print_function, absolute_import

__all__ = ["number_tracks", "genre_weekday"]
__version__ = 0.1
__author__ = "Sergey Polivin"

from typing import Literal

import pandas as pd


def number_tracks(
    data: pd.DataFrame,
    day: Literal["Monday", "Wednesday", "Friday"],
    city: Literal["Moscow", "Saint-Petersburg"],
) -> int:
    """Computes day- and city-specific number of track plays.

    Given the data with users' musical preferences, returns the number
    of tracks played in a particular city on a particular day.

    Args:
        data: DataFrame with information on musical preferences.
        day: Name of a weekday.
        city: Name of a city.

    Returns:
        Integer number of track plays in a given city on a given
        day.
    """
    track_list = data[data["day"] == day]
    track_list = track_list[track_list["city"] == city]

    track_list_count = track_list["user_id"].count()

    return track_list_count


def genre_weekday(
    data: pd.DataFrame,
    day: Literal["Monday", "Friday"],
    time_start: str = "00:00",
    time_end: str = "23:59",
    include_bounds: Literal["neither", "both", "left", "right"] = "neither",
) -> pd.Series:
    """
    Returns a rating of top-10 most popular genres
    on a given day at a given time.

    Args:
        data: DataFrame with information on musical preferences.
        day: Name of a weekday.
        time_start: Lower bound of a time period in "hh:mm" format.
        time_end: Upper bound of a time period in "hh:mm" format.
        include_bounds: Indicator of inclusion of time interval bounds.

    Returns:
        pandas.Series object mapping top-10 most popular music
        genres to their corresponding track plays numbers.
    """
    genre_df = data[data["day"] == day]
    genre_df = genre_df[
        genre_df["time"].between(time_start, time_end, inclusive=include_bounds)
    ]

    # Compiling a rating of the most popular genres
    genre_df_top_10 = (
        genre_df.groupby("genre")["genre"].count().sort_values(ascending=False)
    ).head(10)

    return genre_df_top_10
