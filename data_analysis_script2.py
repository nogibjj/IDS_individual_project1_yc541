
import lib
import pandas as pd

data = lib.load_csv("bestsellers with categories.csv")

# Average number of books each year with reviews over 10,000
high_reviewed_books = data[data['Reviews'] > 10000]
avg_high_reviewed_books = high_reviewed_books.groupby('Year').size().mean()

# Books with highest and lowest reviews over the years
most_reviewed_books = data[data['Reviews'] == data['Reviews'].max()]
least_reviewed_books = data[data['Reviews'] == data['Reviews'].min()]

# Analysis of books by J.K. Rowling
jk_rowling_books = data[data['Author'].str.contains('J.K. Rowling')]

# Correlation between Price and Reviews
corr_price_reviews = lib.get_correlation(data, 'Price', 'Reviews')

# Visualization of the correlation
lib.visualize_correlation(data, 'Price', 'Reviews', 'Price vs. Reviews',"price_vs_reviews.png")

