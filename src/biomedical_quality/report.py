import pandas as pd

def quality_report(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a DataFrame.")
    df_len = len(df)
    if df_len == 0:
        raise ValueError("DataFrame is empty.")
    
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

def class_balance_report(targets: pd.Series, target_names: List) -> pd.DataFrame:

    col_names = ["count", "percentage"]
    target_df = pd.DataFrame(
        columns=col_names,
        index=target_names,
    )
    print(target_df)
    return None