"""This module contains useful data analysis and visualization
tools for categorizing bank clients and recovering hidden patterns
from data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def categorize_purpose(loan_purpose: str) -> str:
    """Classifies people into loan purpose categories depending on loan purpose."""
    loan_purpose = loan_purpose.lower()
    if "автом" in loan_purpose:
        return "Car"
    elif "жил" in loan_purpose or "недвиж" in loan_purpose:
        return "Real estate"
    elif "свад" in loan_purpose:
        return "Wedding"
    elif "образов" in loan_purpose:
        return "Education"
    else:
        return "Other"


def categorize_family_status(family_status: str) -> str:
    """Classifies people into family status categories depending on family status."""
    family_status = family_status.lower()
    if "не жен" in family_status or "не замуж" in family_status:
        return "Unmarried"
    elif "разв" in family_status:
        return "Divorced"
    elif "вдов" in family_status:
        return "Widow(er)"
    elif "гражд" in family_status:
        return "Civil"
    elif "жен" in family_status or "замуж" in family_status:
        return "Married"
    else:
        return "Other"


def show_solvency_by_cat(feature: str, data: pd.DataFrame) -> pd.DataFrame:
    """Displays solvency statistics for borrowers by category of a feature.

    Args:
        feature: Characteristic of borrowers.
        data: Bank clients' data.

    Returns:
        pandas.DataFrame object with solvency statistics for
        each unique element of feature.
    """
    data_grouped = data.groupby(feature).agg({"debt": ["count", "sum"]})

    # Number of borrowers who managed to repay on time
    data_grouped["no_debt"] = (
        data_grouped["debt"]["count"] - data_grouped["debt"]["sum"]
    )

    # Computing debt repayment ratio
    data_grouped["no_debt_share"] = np.round(
        data_grouped["no_debt"] / data_grouped["debt"]["count"], 4
    )

    # Getting rid of multiindex
    data_grouped.columns = [
        "total_borrowers",
        "has_debt",
        "no_debt",
        "repay_ratio",
    ]

    solvency_info = data_grouped.copy()

    return solvency_info


def plot_solvency_by_cat(feature: str, data: pd.DataFrame) -> None:
    """Plots solvency statistics for borrowers by category of `feature`.

    Creates two plots:
        - Left one depicts the number of borrowers who repayed
    and did not repayed the loan for each category within `feature`.
        - Right plot shows debt repayment ratios for each category of
        clients within `feature`.

    Args:
        feature: Characteristic of borrowers.
        data: Bank clients' data.

    Returns:
        Returns None. Plots a figure.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle(f"Solvency of clients by {feature}")

    # Plotting the number of borrowers
    figure_left = sns.barplot(
        x=feature,
        y="debt",
        data=data,
        estimator=lambda x: len(x),
        ci=None,
        hue="debt",
        ax=axes[0],
    )
    axes[0].legend(title="Status", loc="upper right", labels=["Repaid", "In debt"])
    axes[0].set_title("Number of borrowers by categories")
    axes[0].set_ylabel("People")

    # Plotting the debt repayment ratio
    figure_right = sns.barplot(
        x=feature,
        y="debt",
        data=data,
        estimator=lambda x: 100 - sum(x) / len(x) * 100,
        ci=None,
        ax=axes[1],
        color="dodgerblue",
    )
    axes[1].set_title("Repayment rate by categories")
    axes[1].set_ylabel("Percent")

    # Responsively setting y-limits for the right plot
    repay_rate = (
        data.groupby(feature)["debt"].sum() / data.groupby(feature)["debt"].count()
    )
    lower_bound = (100 - 100 * np.max(repay_rate)) - 0.5
    upper_bound = (100 - 100 * np.min(repay_rate)) + 0.5
    axes[1].set_ylim(lower_bound, upper_bound)

    plt.tight_layout()
