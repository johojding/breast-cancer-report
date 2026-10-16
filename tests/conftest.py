import pandas as pd
import pytest

@pytest.fixture
def clean_df():
    return pd.DataFrame({
        "age": [20, 30, 40],
        "score": [5, 5 ,10],
    })