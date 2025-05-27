import pandas as pd
from src.load_data import load_csv

def test_load_csv(tmp_path):
    # Create a small CSV
    file = tmp_path / "test.csv"
    file.write_text("a,b")

  # Header and one data row
    df = load_csv(str(file))
    assert list(df.columns) == ['a', 'b']
