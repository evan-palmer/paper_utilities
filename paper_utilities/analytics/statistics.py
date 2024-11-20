# Copyright 2024, Evan Palmer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from typing import Any, Callable

import numpy as np
import pandas as pd


def calculate_stats(
    data: pd.DataFrame | list[pd.DataFrame], columns: str | list[str]
) -> dict[str, dict[str, dict[str, float | int]]]:
    """Calculate common statistics for specified columns in the provided data.

    Args:
        data: The data to calculate statistics for. Can be a single DataFrame or a list of
            DataFrames.
        columns: The columns to calculate statistics for. Can be a single column name or a
            list of column names.

    Returns:
        A dictionary containing the calculated statistics for each specified column in
        each DataFrame. The dictionary is structured as follows:
            {
                "column_name": {
                    "mean": float,
                    "median": float,
                    "std": float,
                    "min": float,
                    "max": float,
                    "count": int,
                },
                ...
            }
    """
    if isinstance(data, pd.DataFrame):
        data = [data]

    if isinstance(columns, str):
        columns = [columns]

    # Calculate some common statistics for each specified column
    statistics = {}

    for column in columns:
        statistics[column] = {}

        for df in data:
            statistics[column] = {
                "mean": df[column].mean(),
                "median": df[column].median(),
                "std": df[column].std(),
                "min": df[column].min(),
                "max": df[column].max(),
                "count": df[column].count(),
            }

    return statistics


def merge_and_calculate_stats(
    data: list[pd.DataFrame], columns: str | list[str]
) -> dict[str, dict[str, dict[str, float | int]]]:
    """Merge DataFrames and then calculate common statistics for the specified columns.

    Args:
        data: A list of DataFrames to merge and calculate statistics for.
        columns: The columns to calculate statistics for. Can be a single column name or a
            list of column names.

    Returns:
        A dictionary containing the calculated statistics for each specified column in
        the merged DataFrame. The dictionary is structured as follows:
            {
                "column_name": {
                    "mean": float,
                    "median": float,
                    "std": float,
                    "min": float,
                    "max": float,
                    "count": int,
                },
                ...
            }
    """
    merged_data = pd.concat(data, join="inner", axis=0)
    return calculate_stats(merged_data, columns)


def calculate_stats_across_dfs(
    data: list[pd.DataFrame], func: Callable[[pd.DataFrame], Any]
) -> dict[str, Any]:
    """Map a function across the DataFrames and calculate statistics on the results.

    Args:
        data: A list of DataFrames to map the function across.
        func: The function to map across the DataFrames.

    Returns:
        A dictionary containing the calculated statistics for the results of the function
        mapped across the DataFrames. The dictionary is structured as follows:
            {
                "mean": float,
                "median": float,
                "std": float,
                "min": float,
                "max": float,
                "count": int,
    """
    vals = np.array([func(df) for df in data])

    return {
        "mean": np.mean(vals),
        "median": np.median(vals),
        "std": np.std(vals),
        "min": np.min(vals),
        "max": np.max(vals),
        "count": len(vals),
    }
