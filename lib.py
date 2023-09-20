
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def get_correlation(df, col1, col2) -> float:
    return df[col1].corr(df[col2])

def visualize_correlation(df, col1, col2, title, save_path):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=col1, y=col2)
    plt.title(title)
    plt.grid(True)
    plt.savefig(save_path, format='png')
    plt.show()
    plt.close()

def visualize_line_chart(df, x_col, y_col1, y_col2, title, save_path):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col1], marker='o', label=y_col1)
    plt.plot(df[x_col], df[y_col2], marker='o', label=y_col2)
    plt.xlabel(x_col)
    plt.ylabel("Number of Books")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path, format='png')
    plt.show()
    plt.close()
