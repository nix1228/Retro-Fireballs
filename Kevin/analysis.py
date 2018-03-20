# Dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

filename = "Raw_Data/season1.json"
def sentimentify(filename):
    picpath = "Images/" + filename[9:-5]
    
    # Read the file
    with open(filename, "r") as data_file:
        data = json.load(data_file)
    
    # Extract files and set up
    # Set up some empty lists for magic
    topandas = []
    eptitles = []
    
    # First loop through each episode title, stored as keys in the json read into the data variable
    for episode in data.keys():
        
        # Populate eptitles list with episode titles, formatted to be the same as our dictionary later and removing "Game Of Thrones" and ".srt" from each title
        eptitles.append(episode[16:-4])

        # Go through each key (timestamp maybe) and line (text string of the lines being said) per episde
        for key, line in data[episode].items():

            # Run VADER analysis on the line
            results = analyzer.polarity_scores(line)

            # If the line isn't 0 scoring, add it's information as a dictionary to our list of dictionaries to be panda-ified
            if results["compound"] != 0:
                topandas.append({
                    "Ep": episode[16:-4], #Remove Game of Thrones & .srt from string
                    "Line": line,
                    "Compound": results["compound"],
                    "Positive": results["pos"],
                    "Neutral": results["neu"],
                    "Negative": results["neg"],
                    "Sequence": key,
                    "Positive?": results["compound"] > 0
            })
            
    # Make it a dataframe
    df = pd.DataFrame(topandas)

    # Plot each episode
    try:
        plt.close()
        plt.figure(figsize=(18,6))
        plt.ylim(-1.2,1.2)
        sns.violinplot(x='Ep',y='Compound',data=df[df['Ep'].isin(eptitles[:3])],inner=None)
        sns.swarmplot(x="Ep", y="Compound",data=df[df['Ep'].isin(eptitles[:3])], color="black", alpha=.9)
        plt.hlines(0, -10, 10, alpha=.25, linestyle=":")
        plt.xlabel('')
        plt.xticks(size=12)
        plt.ylabel('VADER Compound Sentiment Score',size=15)
        plt.savefig(f'{picpath}_1.png')
        plt.show()
    except ValueError:
        print("No Data to plot.")

    try:
        plt.close()
        plt.figure(figsize=(18,6))
        plt.ylim(-1.2,1.2)
        sns.violinplot(x='Ep',y='Compound',data=df[df['Ep'].isin(eptitles[3:7])],inner=None)
        sns.swarmplot(x="Ep", y="Compound",data=df[df['Ep'].isin(eptitles[3:7])], color="black", alpha=.9)
        plt.hlines(0, -10, 10, alpha=.25, linestyle=":")
        plt.xlabel('')
        plt.xticks(size=12)
        plt.ylabel('VADER Compound Sentiment Score',size=15)
        plt.savefig(f'{picpath}_2.png')
        plt.show()
    except ValueError:
        print("No Data to plot.")

    try:
        plt.close()
        plt.figure(figsize=(18,6))
        plt.ylim(-1.2,1.2)
        sns.violinplot(x='Ep',y='Compound',data=df[df['Ep'].isin(eptitles[7:])],inner=None)
        sns.swarmplot(x="Ep", y="Compound",data=df[df['Ep'].isin(eptitles[7:])], color="black", alpha=.9)
        plt.hlines(0, -10, 10, alpha=.25, linestyle=":")
        plt.xlabel('')
        plt.xticks(size=12)
        plt.ylabel('VADER Compound Sentiment Score',size=15)
        plt.savefig(f'{picpath}_3.png')
        plt.show()
    except ValueError:
        print("No data to plot.")

    print("\nPositive Value VADER Means Table:\n")
    print(df[df['Positive?']==True].groupby('Ep')['Compound'].mean().sort_values(ascending=False)) # Shows how strong positive sentiments are
    
    print("\nNegative Value VADER Means Table:\n")
    print(df[df["Positive?"]==False].groupby("Ep")["Compound"].mean().sort_values(ascending=True)) # Shows how strong negative sentiments are

    print("\nVADER Means Table:\n")
    print(df.groupby("Ep")["Compound"].mean().sort_values(ascending=False)) # Overall Sentiment Means

    # Positive sentiments only mean df
    positive_df = df[df['Positive?']==True].groupby('Ep')['Compound'].mean() #.sort_values(ascending=False)

    # Negative sentiments only mean df
    negative_df = df[df["Positive?"]==False].groupby("Ep")["Compound"].mean() #.sort_values(ascending=True)

    # All sentiments mean df
    mean_df = df.groupby("Ep")["Compound"].mean() #.sort_values(ascending=False)

    colors = ["red", "gray", "yellow", "green", "gold", "black", "blue", "purple", "orange", "pink"]
    edges = ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]

    fig, ax = plt.subplots(figsize=(15, 5))
    pos_rect = ax.bar(np.arange(len(positive_df)), positive_df, color=colors, edgecolor=edges)
    ax.set_xticks(np.arange(len(positive_df)))
    ax.set_xticklabels(positive_df.keys(), rotation = 90)
    ax.set_xlim(-0.5, len(positive_df) - 0.5)

    plt.savefig(f'{picpath}_4.png')
    plt.show()

    plt.close()
    fig, ax = plt.subplots(figsize=(15, 5))
    neg_rect = ax.bar(np.arange(len(negative_df)), negative_df, color=colors, edgecolor=edges)
    ax.set_xticks(np.arange(len(negative_df)))
    ax.set_xticklabels(negative_df.keys(), rotation = 90)
    ax.set_xlim(-0.5, len(positive_df) - 0.5)

    plt.savefig(f'{picpath}_5.png')
    plt.show()

    plt.close()
    fig, ax = plt.subplots(figsize=(15, 5))
    mean_green_rect = ax.bar(np.arange(len(mean_df)), mean_df, color=colors, edgecolor=edges)
    ax.set_xticks(np.arange(len(mean_df)))
    ax.set_xticklabels(mean_df.keys(), rotation = 90)
    ax.set_xlim(-0.5, len(positive_df) - 0.5)

    plt.savefig(f'{picpath}_6.png')
    plt.show()