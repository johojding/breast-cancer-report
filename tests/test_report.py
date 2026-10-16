from biomedical_quality import quality_report
from pytest import raises

def test_clean_data_has_no_missing_values(clean_df):
    report, _ = quality_report(clean_df)

    assert report["missing_count"].sum() == 0

def test_clean_data_has_no_duplicates(clean_df):
    _, duplicates = quality_report(clean_df)

    assert duplicates == 0

def test_missing_data_has_missing_count(missing_df):
    report, _ = quality_report(missing_df)

    assert report["missing_count"].sum() == 1

def test_duplicate_data_has_duplicate_count(duplicated_df):
    _, duplicates = quality_report(duplicated_df)

    assert duplicates == 1

def test_empty_data(empty_df):
    with raises(ValueError):
        quality_report(empty_df)

def test_wrong_input_type():
    with raises(TypeError):
        quality_report(None)
