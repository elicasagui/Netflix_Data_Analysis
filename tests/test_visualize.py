import pandas as pd
from src.visualize import plot_histogram

def test_plot_histogram(monkeypatch):
    df = pd.DataFrame({'col': [1,2,3]})
    # Ensure no errors when plotting
    plot_histogram(df, 'col', bins=3)
