import lib
import pandas as pd
from pytest import approx

def test_load_csv():
    data = lib.load_csv("bestsellers with categories.csv")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_get_correlation():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    assert lib.get_correlation(data, 'A', 'B') == approx(-1.0)
