import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("./credits.csv")
titles = pd.read_csv("./titles.csv")

def task2():
    scores = titles[titles['type'] == "SHOW"]['age_certification'].dropna()
    labels, scores = np.unique(scores, return_counts=True)
    plt.figure(figsize=(10,6))
    plt.pie(scores, labels = labels)
    plt.title("SHOW age rat")


task2()
plt.show()
