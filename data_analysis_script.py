import lib
import pandas as pd

# Load the data
data = lib.load_csv("bestsellers with categories.csv")

# 1. Summary for 2009-2019
rating_per_year = data.groupby('Year')['User Rating'].agg(['mean', 'median'])
fiction_non_fiction_count = data.groupby(['Year', 'Genre']).size().unstack(fill_value=0)
books_above_47 = data[data['User Rating'] > 4.7].groupby(['Year', 'Genre']).size().unstack(fill_value=0)
print("===== Rating Summary =====")
print(rating_per_year)
print("\n===== Fiction & Non-Fiction Book Counts =====")
print(fiction_non_fiction_count)
print("\n===== Book Counts with Rating above 4.7 =====")
print(books_above_47)

# 2. Books with highest and lowest rating across the years
highest_rated_books = data[data['User Rating'] == data['User Rating'].max()]
lowest_rated_books = data[data['User Rating'] == data['User Rating'].min()]
print("\n===== Highest Rated Books =====")
print(highest_rated_books[['Name', 'Author', 'Genre', 'User Rating']])
print("\n===== Lowest Rated Books =====")
print(lowest_rated_books[['Name', 'Author', 'Genre', 'User Rating']])

# 3. Correlation: Rating vs. Reviews and Rating vs. Price
corr_rating_reviews = lib.get_correlation(data, 'User Rating', 'Reviews')
corr_rating_price = lib.get_correlation(data, 'User Rating', 'Price')
print("\n===== Correlation: Rating vs. Reviews =====")
print(f"Correlation coefficient: {corr_rating_reviews}")
print("\n===== Correlation: Rating vs. Price =====")
print(f"Correlation coefficient: {corr_rating_price}")

# Visualizations
lib.visualize_correlation(data, 'User Rating', 'Reviews', 'Rating vs. Reviews', "rating_vs_reviews.png")
lib.visualize_correlation(data, 'User Rating', 'Price', 'Rating vs. Price', "rating_vs_price.png")
lib.visualize_line_chart(books_above_47.reset_index(), 'Year', 'Fiction', 'Non Fiction', 'Books with Rating above 4.7 over the years', "books_above_47_over_years.png")
