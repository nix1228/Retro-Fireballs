
# coding: utf-8

# In[1]:


import requests
import json
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def view_imdb_data_votes(season_number,episode_number):
    url="http://www.omdbapi.com/?t="
    season="&Season="+str(season_number)
    episode="&Episode="+str(episode_number)
    api_key="&apikey=7329004f"
    response=requests.get(url+"Game of Thrones" +season+episode+api_key)
    data=response.json()
    return data["imdbVotes"]


# In[3]:


def view_imdb_data_ratings(season_number,episode_number):
    url="http://www.omdbapi.com/?t="
    season="&Season="+str(season_number)
    episode="&Episode="+str(episode_number)
    api_key="&apikey=7329004f"
    response=requests.get(url+"Game of Thrones" +season+episode+api_key)
    data=response.json()
    return data["imdbRating"]


# In[4]:


#season_one votes
season_one=[]
for y in range(11):
        try:
            season_one.append(view_imdb_data_votes(1,y))
        except:
                continue
    
    


# In[5]:


season_one
for i in range(len(season_one)):
    season_one[i]=int(season_one[i])


# In[6]:


#season_two
season_two=[]
for y in range(11):
        try:
            season_two.append(view_imdb_data_votes(2,y))
        except:
                continue
    


# In[7]:


season_two
for i in range(len(season_two)):
    season_two[i]=int(season_two[i])


# In[8]:


#season_three
season_three=[]
for y in range(11):
    try:
        season_three.append(view_imdb_data_votes(3,y))
    except:
        continue


# In[9]:


season_three
for i in range(len(season_three)):
    season_three[i]=int(season_three[i])


# In[10]:


#season_four
season_four=[]
for y in range(11):
    try:
        season_four.append(view_imdb_data_votes(4,y))
    except:
        continue


# In[11]:


season_four
for i in range(len(season_four)):
    season_four[i]=int(season_four[i])


# In[12]:


#season_five
season_five=[]
for y in range(11):
    try:
        season_five.append(view_imdb_data_votes(5,y))
    except:
        continue


# In[13]:


season_five
for i in range(len(season_five)):
    season_five[i]=int(season_five[i])


# In[14]:


#season 6
season_six=[]
for y in range(11):
    try:
        season_six.append(view_imdb_data_votes(6,y))
    except:
        continue


# In[15]:


season_six
for i in range(len(season_six)):
    season_six[i]=int(season_six[i])


# In[16]:


#season 7
season_seven=[]
for y in range(8):
        try:
            season_seven.append(view_imdb_data_votes(7,y))
        except:
            continue


# In[17]:


for i in range(len(season_seven)):
    season_seven[i]=int(season_seven[i])


# In[18]:


votes_df=pd.DataFrame({"Season 1":season_one,
                        "Season 2":season_two,
                         "Season 3":season_three,
                          "Season 4":season_four,
                          "Season 5":season_five,
                          "Season 6":season_six,
                          })


# In[19]:


votes_df_season_seven=pd.DataFrame({"Season 7":season_seven})


# In[20]:


#now for the ratings
season_one_ratings=[]
for y in range(11):
        try:
            season_one_ratings.append(view_imdb_data_ratings(1,y))
        except:
            continue


# In[21]:


season_one_ratings
for i in range(len(season_one_ratings)):
    season_one_ratings[i]=float(season_one_ratings[i])


# In[22]:


season_two_ratings=[]
for y in range(11):
    try:
        season_two_ratings.append(view_imdb_data_ratings(2,y))
    except:
        continue


# In[23]:


season_two_ratings
for i in range(len(season_two_ratings)):
    season_two_ratings[i]=float(season_two_ratings[i])


# In[24]:


season_three_ratings=[]
for y in range(11):
    try:
        season_three_ratings.append(view_imdb_data_ratings(3,y))
    except:
        continue


# In[25]:


season_three_ratings
for i in range(len(season_three_ratings)):
    season_three_ratings[i]=float(season_three_ratings[i])


# In[26]:


season_four_ratings=[]
for y in range(11):
    try:
        season_four_ratings.append(view_imdb_data_ratings(4,y))
    except:
        continue


# In[27]:


season_four_ratings
for i in range(len(season_four_ratings)):
    season_four_ratings[i]=float(season_four_ratings[i])


# In[28]:


season_five_ratings=[]
for y in range(11):
    try:
        season_five_ratings.append(view_imdb_data_ratings(5,y))
    except:
        continue


# In[29]:


season_five_ratings
for i in range(len(season_five_ratings)):
    season_five_ratings[i]=float(season_five_ratings[i])


# In[30]:


season_six_ratings=[]
for y in range(11):
    try:
        season_six_ratings.append(view_imdb_data_ratings(6,y))
    except:
        continue


# In[31]:


season_six_ratings
for i in range(len(season_six_ratings)):
    season_six_ratings[i]=float(season_six_ratings[i])


# In[32]:


season_seven_ratings=[]
for y in range(8): 
    try:
        season_seven_ratings.append(view_imdb_data_ratings(7,y))
    except:
        continue
    


# In[33]:


for i in range(len(season_seven_ratings)):
    season_seven_ratings[i]=float(season_seven_ratings[i])


# In[34]:


ratings_df=pd.DataFrame({"Season 1":season_one_ratings,
                         "Season 2":season_two_ratings,
                          "Season 3":season_three_ratings,
                          "Season 4":season_four_ratings,
                          "Season 5":season_five_ratings,
                          "Season 6":season_six_ratings,
                           })


# In[35]:


ratings_season_seven_df=pd.DataFrame({"Season 7":season_seven_ratings})


# In[36]:


x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7","Ep.8","Ep.9","Ep.10"]
y_axis=ratings_df["Season 1"]
plt.plot(x_axis,y_axis, label="Season 1",color="black")
y_axis=ratings_df["Season 2"]
plt.plot(x_axis,y_axis, label="Season 2", color="lightcoral")
y_axis=ratings_df["Season 3"]
plt.plot(x_axis,y_axis, label="Season 3", color="lightskyblue")
y_axis=ratings_df["Season 4"]
plt.plot(x_axis,y_axis, label="Season 4", color="red")
y_axis=ratings_df["Season 5"]
plt.plot(x_axis,y_axis, label="Season 5", color="darkblue")
y_axis=ratings_df["Season 6"]
plt.plot(x_axis,y_axis, label="Season 6", color="green")
x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7"]
y_axis=ratings_season_seven_df
plt.plot(x_axis,y_axis, label="Season 7", color="orange")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title("Ratings Per Episode in Each Season")
plt.xlabel("Episode")
plt.ylabel("Rating Score")
plt.savefig("RatingsPerEpisodeinEachSeason")
plt.show()


# In[37]:


x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7","Ep.8","Ep.9","Ep.10"]
y_axis=votes_df["Season 1"]
plt.plot(x_axis,y_axis, label="Season 1",color="black")
y_axis=votes_df["Season 2"]
plt.plot(x_axis,y_axis, label="Season 2",color="lightcoral")
y_axis=votes_df["Season 3"]
plt.plot(x_axis,y_axis, label="Season 3",color="lightskyblue")
y_axis=votes_df["Season 4"]
plt.plot(x_axis,y_axis, label="Season 4",color="red")
y_axis=votes_df["Season 5"]
plt.plot(x_axis,y_axis, label="Season 5",color="purple")
y_axis=votes_df["Season 6"]
plt.plot(x_axis,y_axis, label="Season 6",color="green")
x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7"]
y_axis=votes_df_season_seven
plt.plot(x_axis,y_axis, label="Season 7",color="darkblue")
plt.title("IMdB votes per Episode by Season")
plt.xlabel("Episode Number")
plt.ylabel("Number of Votes Per Episode ")
plt.plot(x_axis,y_axis)
plt.legend()
plt.savefig("IMdBvotesperEpisodebySeason")
plt.show()


# In[38]:


avg_rating_season_one=ratings_df["Season 1"].mean()
avg_rating_season_two=ratings_df["Season 2"].mean()
avg_rating_season_three=ratings_df["Season 3"].mean()
avg_rating_season_four=ratings_df["Season 4"].mean()
avg_rating_season_five=ratings_df["Season 5"].mean()
avg_rating_season_six=ratings_df["Season 6"].mean()
avg_rating_season_seven=ratings_season_seven_df.mean()


# In[39]:


x_axis=["Season 1"]
y_axis=avg_rating_season_one
plt.bar(x_axis,y_axis)
x_axis=["Season 2"]
y_axis=avg_rating_season_two
plt.bar(x_axis,y_axis)
x_axis=["Season 3"]
y_axis=avg_rating_season_three
plt.bar(x_axis,y_axis)
x_axis=["Season 4"]
y_axis=avg_rating_season_four
plt.bar(x_axis,y_axis)
x_axis=["Season 5"]
y_axis=avg_rating_season_five
plt.bar(x_axis,y_axis)
x_axis=["Season 6"]
y_axis=avg_rating_season_six
plt.bar(x_axis,y_axis)
x_axis=["Season 7"]
y_axis=avg_rating_season_seven
plt.bar(x_axis,y_axis)
plt.ylim(6.0,10.0)
plt.title("Average Ratings Per Season")
plt.xlabel("Season")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.savefig("AverageRatingsPerSeason")
plt.show()


# In[40]:


avg_votes_season_one=votes_df["Season 1"].mean()
avg_votes_season_two=votes_df["Season 2"].mean()
avg_votes_season_three=votes_df["Season 3"].mean()
avg_votes_season_four=votes_df["Season 4"].mean()
avg_votes_season_five=votes_df["Season 5"].mean()
avg_votes_season_six=votes_df["Season 6"].mean()
avg_votes_season_seven=votes_df_season_seven.mean()


# In[41]:


x_axis="Season 1"
y_axis=avg_votes_season_one
plt.bar(x_axis,y_axis)
x_axis="Season 2"
y_axis=avg_votes_season_two
plt.bar(x_axis,y_axis)
x_axis="Season 3"
y_axis=avg_votes_season_three
plt.bar(x_axis,y_axis)
x_axis="Season 4"
y_axis=avg_votes_season_four
plt.bar(x_axis,y_axis)
x_axis="Season 5"
y_axis=avg_votes_season_five
plt.bar(x_axis,y_axis)
x_axis="Season 6"
y_axis=avg_votes_season_six
plt.bar(x_axis,y_axis)
x_axis="Season 7"
y_axis=avg_votes_season_seven
plt.bar(x_axis,y_axis)
plt.xticks(rotation=45)
plt.title("Average Votes per Season")
plt.xlabel("Season")
plt.ylabel("Average Number of Votes")
plt.savefig("AverageVotesperSeason")
plt.show()

