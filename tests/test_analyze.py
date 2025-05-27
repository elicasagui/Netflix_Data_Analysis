import pandas as pd
import pytest
from src.analyze import compute_duration_stats

def test_compute_duration_stats():
    df = pd.DataFrame({'duration': [10, 20, 20]})
    stats = compute_duration_stats(df, 'duration')
    assert stats['mean'] == pytest.approx(16.6667, rel=1e-3)
    assert stats['median'] == 20
```python
import pandas as pd
from src.analyze import compute_duration_stats

def test_compute_duration_stats():
    df = pd.DataFrame({'duration': [10, 20, 20]})
    stats = compute_duration_stats(df, 'duration')
    assert stats['mean'] == pytest.approx(16.6667, rel=1e-3)
    assert stats['median'] == 20
