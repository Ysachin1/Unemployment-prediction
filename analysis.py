import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    return pd.read_csv(filepath)

def plot_unemployment_rate(df):
    plt.figure(figsize=(10,6))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=df, marker='o')
    plt.title("Unemployment Rate Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
