import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize DataFrame column names:
      - strip whitespace
      - lowercase
      - replace spaces with underscores
      - remove non-alphanumeric characters
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^\w]', '', regex=True)
    )
    return df

def drop_missing(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """
    Drop rows with missing values in the specified subset of columns.
    If subset is None, drop rows with any missing values.
    """
    return df.dropna(subset=subset)

def parse_dates(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Convert specified columns to datetime dtype.
    """
    df = df.copy()
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df
