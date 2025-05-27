import matplotlib.pyplot as plt

def plot_histogram(df, column: str, bins: int = 20):
    plt.figure()
    plt.hist(df[column].dropna(), bins=bins)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.show()
