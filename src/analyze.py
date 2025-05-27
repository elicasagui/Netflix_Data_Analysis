import pandas as pd

def compute_duration_stats(df: pd.DataFrame, column: str) -> dict:
    """
    Return basic duration stats: mean, median, mode.
    """
    return {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'mode': df[column].mode().iloc[0]
    }
