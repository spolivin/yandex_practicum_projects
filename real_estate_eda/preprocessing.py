"""This module contains functions for conducting
preprocessing for "Real Estate Ads Study" project.

The functions presented are assumed to be used as an
input to `apply()` function.
"""

from __future__ import division

__author__ = "Sergey Polivin"

import pandas as pd


def adjust_locality_name(locality_name: str) -> str:
    """Strips locality type from the full locality name."""
    # Listing possible locality types
    location_types = [
        "поселок городского типа",
        "посёлок городского типа",
        "городской поселок",
        "городской посёлок",
        "поселок при железнодорожной станции",
        "посёлок при железнодорожной станции",
        "поселок станции",
        "посёлок станции",
        "коттеджный посёлок",
        "коттеджный поселок",
        "деревня",
        "садовое товарищество",
        "садоводческое некоммерческое товарищество",
        "поселок",
        "посёлок",
        "село",
    ]
    # Deleting locality type
    try:
        for location_type in location_types:
            if location_type in locality_name:
                locality_name_splitted = locality_name.split(location_type + " ")
                locality_name = locality_name_splitted[-1]
                break
        return locality_name
    except:
        # if NaN, getting replaced with 'Неизвестно' ('Unknown')
        return "Неизвестно"


def adjust_ceiling_height(ceil_height: int) -> int:
    """Adjusts anomalous ceiling heights."""
    try:
        # Adjusting height if height > 10.3m
        if ceil_height > 10.3:
            ceil_height = ceil_height / 10
        return ceil_height
    except:
        # if NaN, doing nothing
        pass


def categorize_floors(df: pd.DataFrame) -> str:
    """Classifies floors into 'first', 'second' and 'other' floor categories."""
    # Working only with two columns
    floors_total = df["floors_total"]
    floor = df["floor"]
    # Returning "first" category
    if floor == 1:
        return "First"
    else:
        # Returning "last" category
        if floor == floors_total:
            return "Last"
        # Returning "other" category
        else:
            return "Other"
