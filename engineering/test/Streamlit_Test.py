#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import streamlit.components.v1 as components


import pymongo
from pymongo import MongoClient

import pandas as pd

import plotly


# In[2]:


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.for_class


# In[3]:


db.list_collection_names()


# In[4]:


cursor = db.for_class.cleaned_data.find()
all_data = list(cursor)


# In[5]:


one_year = all_data[0]
most_recent = all_data[-1]


# In[6]:


one_year_df = pd.DataFrame.from_dict(one_year)
most_recent_df = pd.DataFrame.from_dict(most_recent)


# In[7]:


mask = (one_year_df['effect'] == 'Dangerous')
dangerous_year = one_year_df[mask]

mask = (most_recent_df['effect'] == 'Dangerous')
dangerous_recent = most_recent_df[mask]

# In[24]:


from collections import Counter
drugs_y = []
for i in dangerous_year.drugs_in_text:
    i = i.split()
    for i in i:
        drugs_y.append(i)
counter_y_d = Counter(drugs_y)


# In[27]:


year_danger_df = pd.DataFrame.from_dict(counter_y_d, orient='index').reset_index()


# In[37]:



year_danger_df.rename(columns={ year_danger_df.columns[0]: "drug" , year_danger_df.columns[1]: "frequency" }, inplace = True)
year_danger_df = year_danger_df.sort_values(by=['frequency'], ascending=False)


import plotly.express as px


# In[41]:


fig1 = px.bar(year_danger_df.head(10), x='drug', y='frequency', title='Most Common Drug Terms Associated with Dangerous Effects, One Year')
fig1.update_layout(height=400)



# In[42]:
# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

col1, col2 = st.beta_columns((2,1))

with col1:
    components.html(
    '<h1> Novel Psycoactive Substance Dashboard</h1> '
    '<p> This dashboard is designed to provide insights into drug trends based off of the subreddit <a href=""> Research Chemicals</a>. Using a Natural Language Processing model, I categorize posts into categories; the charts below provide updated analysis of the text.</p>'
    )

with col2:
    st.plotly_chart(fig1,height=400)


# In[ ]:




