import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os

path = os.path.dirname(__file__)
my_file = path+'/for_analysis.csv'
data = pd.read_csv(my_file)

tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                stop_words = 'english',
                                lowercase = True,
                                token_pattern = r'\b[a-zA-Z]{3,}\b',
                                max_df = 0.7, #ignore terms that appear in more than X% of the document 
                                min_df = 4)  #ignore terms that appear in less than X documents
dtm_tf = tf_vectorizer.fit_transform(data.drugsremoved)

tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
dtm_tfidf = tfidf_vectorizer.fit_transform(data.drugsremoved)

# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

ex_label = [e[:30]+"..." for e in data.drugsremoved]
doc_word = tf_vectorizer.fit_transform(data.drugsremoved)
pd.DataFrame(doc_word.toarray(), index=ex_label, columns=tf_vectorizer.get_feature_names()).head(10).reset_index(drop=True, inplace=True)

doc_topic = loaded_model.fit_transform(doc_word)

topics = pd.DataFrame(doc_topic.round(5),
             index = ex_label,
             columns = ["Psycadelic","Euphoric",'Negative','Dangerous'])
topics.reset_index()

maxValueIndexObj = topics.idxmax(axis=1)
topics['effect'] = maxValueIndexObj
topics = topics.reset_index()
combined_df = pd.concat([data, topics], axis = 1)


a_file = open("drugs_corpus.csv", "r")
corpus1 = [s.strip() for s in a_file.readlines()]
drugs_corpus = set(corpus1)

drug_terms = []
for i in data.text:
    new_data = i.split()
    post_filter = []
    for i in new_data:
        if i in drugs_corpus:
            post_filter.append(i)
            #post_filter = remove_duplicate(post_filter)
    post_filter = ' '.join(post_filter)
    drug_terms.append(post_filter)
    
combined_df['drug_terms'] = drug_terms

mask1 = (combined_df['effect'] == 'Dangerous') & (combined_df['drug_terms'] != '')

dangerous = combined_df[mask1]

dangerous_drugs = []
for i in dangerous.drug_terms:
    if i != '':
        i = i.split()
        for i in i:
            dangerous_drugs.append(i)
            
dangerous_df = pd.DataFrame(dangerous_drugs)

import plotly.express as px
fig = px.bar(dangerous_df)
fig.show()

st.write(
'This is a text'
)
st.pyplot(plt)
