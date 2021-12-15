import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect=False)
db = client.new_scrapes
db.list_collection_names()
cursor = db.reddit_data.find()
most_recent = list(cursor)[0]
data = pd.DataFrame.from_dict(most_recent.items())
data.drop(index=data.index[0], 
        axis=0, 
        inplace=True)


st.write(
'~~~help~~~'
)
st.dataframe(data)
