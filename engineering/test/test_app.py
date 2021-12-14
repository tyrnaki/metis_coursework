import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.new_scrapes
cursor = db.reddit_data.find()
most_recent = list(cursor)[-1]
data = pd.DataFrame.from_dict(most_recent, orient='index')
data.rename(columns={data.columns[0]: "text" }, inplace = True)
data = data.reset_index()
data = data.drop(['index'],axis=1)

st.write(
'This is a test'
)
st.pyplot(data)
