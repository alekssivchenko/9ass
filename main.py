import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    credits = pd.read_csv("./credits.csv")
    titles = pd.read_csv("./titles.csv")


    scores = titles[titles['type'] == "MOVIE"]['imdb_score'].dropna()
    scores1 = titles[titles['type'] == "SHOW"]['imdb_score'].dropna()
    figure = plt.figure(figsize=(16, 6))
    #plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.hist(scores1, np.arange(0, 10.2, 0.2))
    #scores2 = titles.groupby(by=['type'])['imdb_score'].mean()
    #print(scores2)
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth='2')
    plt.xlabel("Score")
    plt.ylabel("Num")
    plt.title("Scores counted")
    plt.show()
    #plt.savefig(fname='plot1.png')




main()
