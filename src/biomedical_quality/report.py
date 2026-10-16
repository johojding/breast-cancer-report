import pandas as pd
import numpy as np

def quality_report(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    _validate_dataframe(df)
    _validate_not_empty(df)

    df_len = len(df)
    col_names = ["dtype", "missing_count", "missing_pct", "unique_count", "unique_pct", "mean", "std", "min", "25_percentile", "median", "75_percentile", "max"]
    report_df = pd.DataFrame(
        columns=col_names,
        index=df.columns
        )                                   # create new dataframe

    report_df["dtype"] = df.dtypes          # add dtypes

    report_df["missing_count"] = df.isna().sum()            # missing
    report_df["missing_pct"] = (report_df["missing_count"] / df_len * 100)

    report_df["unique_count"] = df.nunique()                # unique
    report_df["unique_pct"] = (report_df["unique_count"] / df_len * 100)

    report_df["mean"] = df.mean(numeric_only=True)              # mean
    report_df["std"] = df.std(numeric_only=True)                # standard deviation
    report_df["min"] = df.min(numeric_only=True)                # minimum
    report_df["max"] = df.max(numeric_only=True)                # maximum
    report_df["median"] = df.median(numeric_only=True)          # median
    report_df["25_percentile"] = df.quantile(0.25, numeric_only=True)      # 25th percentile
    report_df["75_percentile"] = df.quantile(0.75, numeric_only=True)      # 75th percentile

    nr_duplicates = df.duplicated().sum()
    return report_df, nr_duplicates

def class_balance_report(targets: pd.Series, target_names: list[str] | np.ndarray) -> pd.DataFrame:
    _validate_series(targets)
    _validate_target_names(target_names)
    _validate_not_empty(targets, target_names)

    label_map = dict(enumerate(target_names))
    labels = targets.map(label_map)

    col_names = ["count", "percentage"]
    target_df = pd.DataFrame(
        columns=col_names
    )

    target_df["count"] = labels.value_counts()      # counts of target
    target_df["percentage"] = target_df["count"] / len(targets) * 100       # percentages

    return target_df


def _validate_dataframe(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a DataFrame.")

def _validate_series(s: pd.Series):
    if not isinstance(s, pd.Series):
        raise TypeError("Input data must be a Series.")

def _validate_target_names(l):
    if not isinstance(l, (list, np.ndarray)):
        raise TypeError("Input data must be a list or NumPy array.")

def _validate_not_empty(*args):
    for obj in args:
        if len(obj) == 0:
            raise ValueError("Input is empty.")