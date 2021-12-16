#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import streamlit.components.v1 as components


import pymongo
from pymongo import MongoClient

import pandas as pd

import plotly
import plotly.express as px
from collections import Counter

import datetime
from datetime import datetime, date
from dateutil.relativedelta import relativedelta # to add days or years


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
#today = all_data[-1]
#yesterday = all_data[-2]


# In[6]:


one_year_df = pd.DataFrame.from_dict(one_year)
dates = []
for i in one_year_df.timestamp:
        i = i[:10]
        dates.append(datetime.strptime(i, '%Y-%m-%d').date())
one_year_df['dates'] = dates
#today_df = pd.DataFrame.from_dict(today)
#yesterday_df = pd.DataFrame.from_dict(yesterday)


#mask = (today_df['drugs_in_text'] != '')
#most_recent_df_effect = today_df[mask]
#drugs_today = most_recent_df_effect.filter(['drugs_in_text','effect'], axis=1).reset_index().drop(['index'],axis=1)


# In[24]:

def reaction_masker(x, y, z):
	mask = (y <= one_year_df['dates']) & (one_year_df['dates'] <= z) & (one_year_df['effect'] == x)
	return one_year_df[mask]

def drugs_counter(x):
	drugs_y = []
	for i in x:
	    i = i.split()
	    for i in i:
	        drugs_y.append(i)
	counter_y_d = Counter(drugs_y)
	df = pd.DataFrame.from_dict(counter_y_d, orient='index').reset_index()
	df.rename(columns={ df.columns[0]: "drug" , df.columns[1]: "frequency" }, inplace = True)
	return df.sort_values(by=['frequency'], ascending=False)

def drug_definer(x):
    drug_links_list = ""
    for i in x:
        link = 'https://www.google.com/search?q='+i
        drug_string = '**['+i+']('+link+')**'
        drug_links_list+drug_string
    return drug_links_list

def drug_lister(x):
    drug_list = []
    for i in x:
        drug_list.append(i)
    return drug_list

def grab_post(x, selection_for_post):
    mask = x['drugs_in_text'].str.contains(selection_for_post)
    new_df = x[mask]
    return new_df['text'][0]
# In[42]:
st.set_page_config(layout="wide")

st.title('Novel Psychoactive Substance Monitoring Dashboard')
st.write('This dashboard is designed to provide insights into Novel Psychoactive Substance (NPS) trends based off of the subreddit [Research Chemicals](https://www.reddit.com/r/researchchemicals/). This application uses a Natural Language Processing model to categorize Reddit posts and related drug terms; the charts below provide regularly updated analysis of the text.')

col1, col2, col3= st.columns((2,0.25,1))

with col1:
	#cols1,_= st.columns((3,1)) # To make it narrower
	st.subheader('Reactions to NPS:')
	selection = st.selectbox(
	     'Choose a reaction',
	     ('Dangerous', 'Negative', 'Euphoric', 'Psycadelic'))

	format = 'MMM DD, YYYY'  # format output
	start_date = datetime.now().date()-relativedelta(years=1)  #  I need some range in the past
	end_date = datetime.now().date()
	max_days = end_date-start_date
	        
	values = st.slider('Select a timeframe', start_date, end_date, (start_date, end_date))
	#slider = col1.slider('Select date', min_value=start_date, value=end_date ,max_value=end_date, format=format)
	        ## Sanity check
	#start_date_t = type(end_date)

	
	values_selected_start, values_selected_end = values
	selected_start_date = values_selected_start.strftime("%b %d %Y")
	selected_end_date = values_selected_end.strftime("%b %d %Y")

	one_year_df = reaction_masker(selection, values_selected_start, values_selected_end)
	year_df = drugs_counter(one_year_df.drugs_in_text)

	one_year_chart = px.bar(year_df.head(10), x='drug', y='frequency', title='Most Common Drug Terms Associated with '+ selection + ' Effects, from '+selected_start_date+' to '+selected_end_date)
	one_year_chart.update_layout(height=400)

	st.plotly_chart(one_year_chart, height=500)

	st.subheader('What does a '+selection.lower()+' reaction look like with*:')
	selection_for_post = st.selectbox(
	     'Choose a substance',
	     (drug_lister(year_df['drug'].head(10))))
	st.markdown('***note: these are unedited reddit posts and may contain NSW language**')
	st.markdown(grab_post(one_year_df, selection_for_post))

with col2:
	st.text('')

with col3:
	st.subheader('What are these substances?')
	st.markdown('The listed substances below correspond to the chart on the lef, click on each to find out more.')
	drug_links = drug_definer(year_df['drug'].head(10))
	st.markdown(drug_links)



# In[ ]:




