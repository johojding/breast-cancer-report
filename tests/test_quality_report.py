import pandas as pd
from biomedical_quality import quality_report

def test_clean_data_has_no_missing_values(clean_df):
    report, duplicates = quality_report(clean_df)

    assert report["missing_count"].sum() == 0
    assert duplicates == 0
