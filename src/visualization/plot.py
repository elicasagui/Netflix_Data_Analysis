import matplotlib.pyplot as plt
import seaborn as sns

def plot_duration_distribution(df, column='duration', bins=20, figsize=(10, 6)):
    """
    Plot a histogram of movie durations.
    """
    plt.figure(figsize=figsize)
    sns.histplot(df[column], bins=bins, kde=False)
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Count')
    plt.title('Distribution of Movie Durations in the 1990s')
    plt.tight_layout()
    plt.show()

def plot_short_action_count(count, figsize=(6, 4)):
    """
    Plot a single-bar chart showing the count of short action movies.
    """
    plt.figure(figsize=figsize)
    sns.barplot(x=['Short Action Movies (<90 min)'], y=[count])
    plt.ylabel('Count')
    plt.title('Count of Short Action Movies in the 1990s')
    plt.tight_layout()
    plt.show()
