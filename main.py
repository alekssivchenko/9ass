import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("./credits.csv")
titles = pd.read_csv("./titles.csv")


def fig_1():
    scores = titles[titles['type'] == "MOVIE"]['imdb_score'].dropna()
    figure = plt.figure(figsize=(16, 6))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth='2')
    plt.xlabel("Score")
    plt.ylabel("Num")
    plt.title("MOVIE")
    #plt.savefig(fname='plot1.png')

def fig_2():
    scores = titles[titles['type'] == "SHOW"]['imdb_score'].dropna()
    figure = plt.figure(figsize=(16, 6))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth='2')
    plt.xlabel("Score")
    plt.ylabel("Num")
    plt.title("SHOW")

def mean():
    print(titles.groupby(by=["type"])["imdb_score"].mean())
    mean1 = titles[titles["type"] == "SHOW"]["imdb_score"].mean()
    mean2 = titles[titles["type"] == "MOVIE"]["imdb_score"].mean()
    if mean2 > mean1:
        print("MOVIE average is greater")
    else:
        print("SHOW average is greater")

def task1():
    global titles
    bins = np.arange(0, 10 + 0.2, 0.2)
    hists = titles.hist(column='imdb_score', by='type', bins=bins, linewidth=0.5, xlabelsize=5)
    for hist in hists:
            hist.set_xticks(bins)
            hist.grid()

task1()
mean()
plt.show()
