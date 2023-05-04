"""This module contains functions for data preprocessing."""

from __future__ import division, print_function, absolute_import

__author__ = "Sergey Polivin"

from typing import Optional

import pandas as pd


def identify_missing_values(data: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Computes a number and share of missing values
    in DataFrame columns which have NaN-values present
    and displays data types of such columns.

    Args:
        data: DataFrame.

    Returns:
        pandas.DataFrame object with column names, number of
        missing values and shares of NaN-values in such columns.
        In case there are not missing values present, an according
        message is shown and nothing is returned.
    """
    # Verifying missing values
    miss_vals_num = data.isnull().sum()[data.isnull().sum() > 0]
    if miss_vals_num.empty == True:
        print("Missing values are not found.")
        return
    # Creating a table with numbers of missing values
    cols = {"missing_count": miss_vals_num.values}
    nans_df = pd.DataFrame(data=cols, index=miss_vals_num.index).sort_values(
        by="missing_count", ascending=False
    )
    # Adding shares of missing values
    nans_df["missing_fraction"] = nans_df["missing_count"] / data.shape[0]
    nans_df["missing_fraction"] = nans_df["missing_fraction"].round(4)
    # Adding data types
    nans_df["dtype"] = data[nans_df.index].dtypes
    nans_df = nans_df[["dtype", "missing_count", "missing_fraction"]]

    return nans_df


def identify_duplicates(data: pd.DataFrame) -> None:
    num_duplicates = data.duplicated().sum()
    if num_duplicates != 0:
        data.drop_duplicates(inplace=True)
        print(f"{num_duplicates:,} duplicates found and deleted.")
    else:
        print("No duplicates found.")
