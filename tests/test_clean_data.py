import pandas as pd
from src.clean_data import clean_column_names, drop_missing, parse_dates

def test_clean_column_names():
    df = pd.DataFrame({' A A ': [1], 'B!': [2]})
    out = clean_column_names(df)
    assert 'a_a' in out.columns
    assert 'b' in out.columns

def test_drop_missing():
    df = pd.DataFrame({'a': [1, None]})
    out = drop_missing(df, subset=['a'])
    assert len(out) == 1

def test_parse_dates():
    df = pd.DataFrame({'d': ['2020-01-01', 'invalid']})
    out = parse_dates(df, cols=['d'])
    assert pd.api.types.is_datetime64_any_dtype(out['d'])
