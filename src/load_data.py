import os
import pandas as pd

# Default data path
DEFAULT_CSV = os.path.join(os.path.dirname(__file__), '..', 'data', 'netflix_data.csv')

def load_csv(path: str = DEFAULT_CSV) -> pd.DataFrame:
    """
    Load CSV into a DataFrame.
    """
    return pd.read_csv(path)
