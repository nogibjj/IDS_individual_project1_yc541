import lib
import pandas as pd

def test_load_csv():
    data = lib.load_csv("bestsellers with categories.csv")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_books_count_per_year():
    data = lib.load_csv("bestsellers with categories.csv")
    high_reviewed_books = data[data['Reviews'] > 10000]
    books_count_per_year = high_reviewed_books.groupby('Year').size()
    expected_counts = {2009: 5, 2010: 8, 2011: 12, 2012: 23, 2013: 20, 2014: 26, 2015: 24, 2016: 28, 2017: 26, 2018: 26, 2019: 27}
    assert books_count_per_year.to_dict() == expected_counts

def test_jk_rowling_books_count():
    data = lib.load_csv("bestsellers with categories.csv")
    jk_rowling_books = data[data['Author'].str.contains('J.K. Rowling')]
    assert jk_rowling_books.shape[0] == 6

def test_corr_price_reviews():
    data = lib.load_csv("bestsellers with categories.csv")
    correlation = lib.get_correlation(data, 'Price', 'Reviews')
    assert -0.2 < correlation < 0.2
