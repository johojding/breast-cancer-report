import pandas as pd

def quality_report(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    df_shape = df.shape
    col_names = ["dtype", "missing_count", "missing_pct", "unique_count", "unique_pct", "mean", "std", "min", "25_percentile", "median", "75_percentile", "max"]
    report_df = pd.DataFrame(
        columns=col_names,
        index=df.columns
        )                                   # create new dataframe

    report_df["dtype"] = df.dtypes          # add dtypes

    report_df["missing_count"] = df.isna().sum()            # missing
    report_df["missing_pct"] = (report_df["missing_count"] / df_shape[0] * 100).round(2)

    report_df["unique_count"] = df.nunique()                # unique
    report_df["unique_pct"] = (report_df["unique_count"] / df_shape[0] * 100).round(2)

    report_df["mean"] = df.mean().round(3)              # mean
    report_df["std"] = df.std().round(3)                # standard deviation
    report_df["min"] = df.min().round(3)                # minimum
    report_df["max"] = df.max().round(3)                # maximum
    report_df["median"] = df.median().round(3)          # median
    report_df["25_percentile"] = df.quantile(0.25).round(2)      # 25th percentile
    report_df["75_percentile"] = df.quantile(0.75).round(2)      # 75th percentile

    nr_duplicates = df.duplicated().sum()
    return report_df, nr_duplicates