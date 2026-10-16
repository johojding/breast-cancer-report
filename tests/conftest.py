import pandas as pd
import pytest

@pytest.fixture
def clean_df():
    return pd.DataFrame({
        "age": [20, 30, 40],
        "score": [5, 5 ,10],
    })

@pytest.fixture
def missing_df():
    return pd.DataFrame({
        "age": [20, None, 40],
        "score": [5, 5, 10],
    })

@pytest.fixture
def duplicated_df():
    return pd.DataFrame({
        "age": [20, 20, 40],
        "score": [5, 5, 10],
    })

@pytest.fixture
def empty_df():
    return pd.DataFrame()