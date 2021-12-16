import praw
import pymongo
from pymongo import MongoClient
import json
import pandas as pd

reddit = praw.Reddit(client_id='X6OHhwJW1MsEi9OIA_e_YA', client_secret='7J31PixC3u63zoNRFLquYSfRBLvlBQ', user_agent='WTyrna_Scrape')


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.new_scrapes

posts = []
ml_subreddit = reddit.subreddit('researchchemicals')
for post in ml_subreddit.new(limit=100):
    posts.append([post.id, post.selftext])
posts = pd.DataFrame(posts,columns=['id', 'body'])

submissions = []
for post in posts.id:
    submission = reddit.submission(id=post)
    for top_level_comment in submission.comments:
        submissions.append([post, top_level_comment.body])

comments = pd.DataFrame(submissions, columns = ['id', 'body'])
one_day_combined = pd.concat([posts, comments])
result=db.reddit_data.insert_one(one_day_combined_dict)
