import pandas as pd
from src.clean_data import clean_column_names

def test_clean_column_names():
    df = pd.DataFrame({' A A ': [1], 'B!': [2]})
    out = clean_column_names(df)
    assert 'a_a' in out.columns
    assert 'b' in out.columns
