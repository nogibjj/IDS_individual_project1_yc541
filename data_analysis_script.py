import lib

data = lib.load_csv("bestsellers with categories.csv")

print("===== Analysis Report =====\n")

# Number of books each year with reviews over 10,000
high_reviewed_books = data[data['Reviews'] > 10000]
books_count_per_year = high_reviewed_books.groupby('Year').size()
print("Number of books with reviews over 10,000 for each year:")
print(books_count_per_year)
print("\n")

# Books with highest and lowest reviews over the years
most_reviewed_books = data[data['Reviews'] == data['Reviews'].max()]
least_reviewed_books = data[data['Reviews'] == data['Reviews'].min()]

print("Books with the most reviews over the years:")
print(most_reviewed_books[['Name', 'Author', 'Reviews']])
print("\nBooks with the least reviews over the years:")
print(least_reviewed_books[['Name', 'Author', 'Reviews']])
print("\n")

# Analysis of books by J.K. Rowling
jk_rowling_books = data[data['Author'].str.contains('J.K. Rowling')]
average_rating_rowling = jk_rowling_books['User Rating'].mean()
print(f"Average rating of J.K. Rowling books: {average_rating_rowling:.2f}")
print(f"Total number of J.K. Rowling books: {jk_rowling_books.shape[0]}")
print("\n")

# Correlation between Price and Reviews
corr_price_reviews = lib.get_correlation(data, 'Price', 'Reviews')
print(f"Correlation between Price and Reviews: {corr_price_reviews:.2f}\n")

# Analysis of average book price change over the years
average_price_per_year = data.groupby('Year')['Price'].mean()
print("Average book price over the years:")
print(average_price_per_year)
print("\n")

# Comparison of average rating between J.K. Rowling books and other books
other_books = data[~data['Author'].str.contains('J.K. Rowling')]
average_rating_others = other_books['User Rating'].mean()
print(f"Average rating of other books: {average_rating_others:.2f}\n")

# Visualization of the correlation
lib.visualize_correlation(data,'Price','Reviews','Price vs. Review',"price-reviews.png")

print("Visualization saved as price_vs_reviews.png")
