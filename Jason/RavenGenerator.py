# Dependencies

import pandas as pd
import numpy as np
import json

filenames = ['Raw_Data/Season1.json',
             'Raw_Data/Season2.json',
             'Raw_Data/Season3.json',
             'Raw_Data/Season4.json',
             'Raw_Data/Season5.json',
             'Raw_Data/Season6.json',
             'Raw_Data/Season7.json']
keywords = ('raven','message')
lines = []

for filename in filenames:
    # Read the file
    with open(filename, "r") as data_file:
        data = json.load(data_file)
        
    # First loop through each episode title, stored as keys in the json read into the data variable
    for episode in data.keys():
        
        # Go through each key (timestamp maybe) and line (text string of the lines being said) per episde
        for key, line in data[episode].items():

            if any(keyword in line.lower() for keyword in keywords):
                lines.append({
                    "Episode": episode[16:-4],
                    "quote_season": episode[1:2],
                    "quote_episode": episode[4:5],
                    "Key": key,
                    "Line": line
                })
message_df = pd.DataFrame.from_dict(lines)
message_df.quote_season = pd.to_numeric(message_df.quote_season, errors='coerce')
message_df.quote_episode = pd.to_numeric(message_df.quote_episode, errors='coerce')
message_df.to_csv("RavensGenerated.csv", sep=',', encoding='utf-8', index=True)