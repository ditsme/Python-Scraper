#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date, datetime, timedelta

#define all the lists
songs_list=[]
songs_rank=[]
songs_artist=[]
songs_last=[]
week_date=[]

#Function to iterate over a time span 
def datespan(startDate, endDate, delta=timedelta(days=7)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta
        
#Get weekly songs from 01-01-2000 to 13-02-2021
for day in datespan(date(2020, 1,4), date(2021, 1, 2),delta=timedelta(days=7)):
    #considering only top 10 songs
    for i in range(0,10):
        week_date.append(day)
        #print(week_date)   
    final_date=day.strftime("%Y-%m-%d")
    URL="https://www.billboard.com/charts/hot-100/"+final_date
    #print(URL)
    content = requests.get(URL)
    soup = BeautifulSoup(content.text, 'html.parser')
    song_names = soup.find_all('span',{ "class" : "chart-element__information__song text--truncate color--primary"},limit=10)
    for row in song_names: 
        songs_list.append(row.text)
    song_rank = soup.find_all('span',{ "class" : "chart-element__rank__number"},limit=10)
    for row1 in song_rank: 
        songs_rank.append(row1.text)
    song_artist = soup.find_all('span',{ "class" : "chart-element__information__artist text--truncate color--secondary"},limit=10)
    for row2 in song_artist:
        songs_artist.append(row2.text)
    song_last_week = soup.find_all('span',{ "class" : "chart-element__meta text--center color--secondary text--last"},limit=10)
    for row3 in song_last_week:  
        songs_last.append(row3.text)
    df = pd.DataFrame({'Week Date':week_date,'Song Name':songs_list,'Song Artist':songs_artist,'Current Week Rank':songs_rank,'Last Week Rank':songs_last}) 
    df.to_csv('songs2.csv', mode='a', index=False, encoding='utf-8',header=False)


# In[ ]:




