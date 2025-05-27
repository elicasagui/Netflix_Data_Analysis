import os
import pandas as pd

# Ruta por defecto al CSV (puedes cambiarla si mueves el archivo)
DEFAULT_CSV_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'netflix_data.csv')

def load_csv(path: str = DEFAULT_CSV_PATH) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    
    Parameters
    ----------
    path : str
        Filesystem path to the CSV file.
    
    Returns
    -------
    pd.DataFrame
    """
    return pd.read_csv(path)

def load_parquet(path: str) -> pd.DataFrame:
    """
    Load a Parquet file into a pandas DataFrame.
    
    Parameters
    ----------
    path : str
        Filesystem path to the Parquet file.
    
    Returns
    -------
    pd.DataFrame
    """
    return pd.read_parquet(path)
