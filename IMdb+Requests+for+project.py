
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


#season_one
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


season_one


# In[7]:


#season_two
season_two=[]
for y in range(11):
        try:
            season_two.append(view_imdb_data_votes(2,y))
        except:
                continue
    


# In[8]:


season_two
for i in range(len(season_two)):
    season_two[i]=int(season_two[i])


# In[9]:


season_two


# In[10]:


#season_three
season_three=[]
for y in range(11):
    try:
        season_three.append(view_imdb_data_votes(3,y))
    except:
        continue


# In[11]:


season_three
for i in range(len(season_three)):
    season_three[i]=int(season_three[i])


# In[12]:


season_three


# In[13]:


#season_four
season_four=[]
for y in range(11):
    try:
        season_four.append(view_imdb_data_votes(4,y))
    except:
        continue


# In[14]:


season_four
for i in range(len(season_four)):
    season_four[i]=int(season_four[i])


# In[15]:


season_four


# In[16]:


#season_five
season_five=[]
for y in range(11):
    try:
        season_five.append(view_imdb_data_votes(5,y))
    except:
        continue


# In[17]:


season_five
for i in range(len(season_five)):
    season_five[i]=int(season_five[i])


# In[18]:


season_five


# In[19]:


#season 6
season_six=[]
for y in range(11):
    try:
        season_six.append(view_imdb_data_votes(6,y))
    except:
        continue


# In[20]:


season_six
for i in range(len(season_six)):
    season_six[i]=int(season_six[i])


# In[21]:


season_six


# In[22]:


#season 7
season_seven=[]
for y in range(8):
        try:
            season_seven.append(view_imdb_data_votes(7,y))
        except:
            continue


# In[23]:


season_seven.append('0')
season_seven.append('0')
season_seven.append('0')
season_seven


# In[24]:


for i in range(len(season_seven)):
    season_seven[i]=int(season_seven[i])


# In[25]:


season_seven


# In[26]:


votes_df=pd.DataFrame({"Season 1":season_one,
                        "Season 2":season_two,
                         "Season 3":season_three,
                          "Season 4":season_four,
                          "Season 5":season_five,
                          "Season 6":season_six,
                          "Season 7":season_seven})


# In[27]:


votes_df


# In[28]:


season_one_ratings=[]
for y in range(11):
        try:
            season_one_ratings.append(view_imdb_data_ratings(1,y))
        except:
            continue


# In[29]:


season_one_ratings
for i in range(len(season_one_ratings)):
    season_one_ratings[i]=float(season_one_ratings[i])


# In[30]:


season_one_ratings


# In[31]:


season_two_ratings=[]
for y in range(11):
    try:
        season_two_ratings.append(view_imdb_data_ratings(2,y))
    except:
        continue


# In[32]:


season_two_ratings
for i in range(len(season_two_ratings)):
    season_two_ratings[i]=float(season_two_ratings[i])


# In[33]:


season_two_ratings


# In[34]:


season_three_ratings=[]
for y in range(11):
    try:
        season_three_ratings.append(view_imdb_data_ratings(3,y))
    except:
        continue


# In[35]:


season_three_ratings
for i in range(len(season_three_ratings)):
    season_three_ratings[i]=float(season_three_ratings[i])


# In[36]:


season_three_ratings


# In[37]:


season_four_ratings=[]
for y in range(11):
    try:
        season_four_ratings.append(view_imdb_data_ratings(4,y))
    except:
        continue


# In[38]:


season_four_ratings
for i in range(len(season_four_ratings)):
    season_four_ratings[i]=float(season_four_ratings[i])


# In[39]:


season_four_ratings


# In[40]:


season_five_ratings=[]
for y in range(11):
    try:
        season_five_ratings.append(view_imdb_data_ratings(4,y))
    except:
        continue


# In[41]:


season_five_ratings
for i in range(len(season_five_ratings)):
    season_five_ratings[i]=float(season_five_ratings[i])


# In[42]:


season_five_ratings


# In[43]:


season_six_ratings=[]
for y in range(11):
    try:
        season_six_ratings.append(view_imdb_data_ratings(4,y))
    except:
        continue


# In[44]:


season_six_ratings
for i in range(len(season_six_ratings)):
    season_six_ratings[i]=float(season_six_ratings[i])


# In[45]:


season_six_ratings


# In[46]:


season_seven_ratings=[]
for y in range(8): 
    try:
        season_seven_ratings.append(view_imdb_data_ratings(7,y))
    except:
        continue
    


# In[47]:


season_seven_ratings.append(0)
season_seven_ratings.append(0)
season_seven_ratings.append(0)


# In[48]:


for i in range(len(season_seven_ratings)):
    season_seven_ratings[i]=float(season_seven_ratings[i])


# In[49]:


season_seven_ratings


# In[50]:


ratings_df=pd.DataFrame({"Season 1":season_one_ratings,
                         "Season 2":season_two_ratings,
                          "Season 3":season_three_ratings,
                          "Season 4":season_four_ratings,
                          "Season 5":season_five_ratings,
                          "Season 6":season_six_ratings,
                           "Season 7":season_seven_ratings})


# In[51]:


ratings_df


# In[52]:


ratings_df["Season 1"]


# In[53]:


x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7","Ep.8","Ep.9","Ep.10"]
y_axis=ratings_df["Season 1"]


# In[62]:


plt.plot(x_axis,y_axis, label="Season 1",color="gold")
y_axis=ratings_df["Season 2"]
plt.plot(x_axis,y_axis, label="Season 2",color="lightcoral")
y_axis=ratings_df["Season 3"]
plt.plot(x_axis,y_axis, label="Season 3",color="lightskyblue")
y_axis=ratings_df["Season 4"]
plt.plot(x_axis,y_axis, label="Season 4",color="red")
y_axis=ratings_df["Season 5"]
plt.plot(x_axis,y_axis, label="Season 5",color="purple")
y_axis=ratings_df["Season 6"]
plt.plot(x_axis,y_axis, label="Season 6",color="green")
y_axis=ratings_df["Season 7"]
plt.plot(x_axis,y_axis, label="Season 7",color="orange")
plt.ylim(7,10.0)
plt.legend()
plt.show()


# In[55]:


x_axis=["Ep.1","Ep.2","Ep.3","Ep.4","Ep.5","Ep.6","Ep.7","Ep.8","Ep.9","Ep.10"]
y_axis=votes_df["Season 1"]


# In[56]:


plt.plot(x_axis,y_axis, label="Season 1",color="gold")
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
y_axis=votes_df["Season 7"]
plt.plot(x_axis,y_axis, label="Season 7",color="orange")
plt.legend()
plt.show()
plt.plot(x_axis,y_axis)
plt.show()

