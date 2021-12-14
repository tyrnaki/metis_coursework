#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import pandas as pd
import matplotlib as plt
import regex as re
#import string as string
from pprint import pprint

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, WordNetLemmatizer

from warnings import filterwarnings
filterwarnings('ignore')

import pymongo
from pymongo import MongoClient

import streamlit as st
import pickle
import plotly


# In[2]:


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


# In[3]:


client.database_names()


# In[4]:


db = client.new_scrapes


# In[5]:


cursor = db.reddit_data.find()
all_data = list(cursor)


# In[6]:


data = []
for i in all_data[0].values():
    data.append(i)
data = pd.DataFrame(data)
data.rename(columns={ data.columns[0]: "text" }, inplace = True)


# In[7]:


split_text = []
for i in data.text:
    text = str(i).split()
    split_text.append(text)
data['split_text'] = split_text

counter = []
for i in data.split_text:
    counter.append(len(i))
data['counter'] = counter

mask = (data['counter'] > 100)
data2 = data[mask]


# In[8]:


data2


# In[9]:


#### make lowercase and remove punctuation

alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())

data2['text'] = data2.text.map(alphanumeric).map(punc_lower)


# In[10]:


def make_corpus(x):
    a_file = open(x, "r")
    corpus = [s.strip() for s in a_file.readlines()]
    a_file.close()
    return corpus


# In[11]:


corpus1 = make_corpus('stop_words_english.txt')
corpus2 = make_corpus("google-10000-english-usa.txt")
big_corpus = corpus1 + corpus2


# In[12]:


stemmer = SnowballStemmer('english')


# In[13]:


####create initial filter, apply stemming

filtered = []
for i in data2.text:
    new_data = i.split()
    post_filter = []
    for i in new_data:
        if i not in corpus1:
            i = stemmer.stem(i)        
            if i not in corpus2:
                post_filter.append(i)
    post_filter = ' '.join(post_filter)
    filtered.append(post_filter)
data2['general_words_removed'] = filtered


# In[14]:


drug_corpus_clean = ['amphetamine', 'clonazolam', 'dopamine', 'methylphenidate', 'bromazolam', 'triptamine', 'dmt', 'mxe', 'fxe', 'flubromazolam',
 'triazolam', 'flualprazolam', 'arylcyclohexylamine', 'acetone', 'chloride', 'etizolam', 'alprazolam',
 'dinotrogen', 'dpt', 'dck', 'bromazepam', 'lorazepam', 'trazodone', 'mirtazapine', 'ketamine', 'klonopin', 'propranolol',
 'fluclotizolam', 'diclazepam', 'norflurazepam', 'quetiapine', 'xan', 'hydrochloride', 'aplrazolam', 'phenethylamine', 'bretazenil', 'rilmazafone', 'pyrazolam', 'emoxypine', 'fasoracetam', 'mda', 'tyrosine', 'diazepam', 'phenylpiracetam', 'pvp', 'flunitrazolam', 'cyclazodone',
 'thc', 'dexamphetamine', 'benzene', 'piracetam', 'benzodiazepine', 'diazepine', 'tryptamine', 'diclaz',
 'metizolam', 'flubrotizolam', 'mescaline', 'hydroxytryptamine', 'dimethyltryptamine', 'clonazepam', 'clonzolam', 'doxylamine', 'diphenydramine',
 'ket', 'allylescaline', 'phenylethylamine', 'oxy', 'nitrazolam', 'clonozolam', 'dopamine',
 'etazene', 'methylamphetamine', 'phenidate', 'mth', 'dextroamphetamine', 'midazolam', 'methamphetamine',
 'fluoroamphetamine', 'ethyltryptamine', 'ethylamine', 'flouromethamphetamine', 'methoxetamine', 'cyclaz', 'zylofuramine', 'cypenamine', 'ephenidine', 'ketamine', 'flumazenil', 'xtc',
 'monoamine', 'methallylescaline', 'methallyescaline', 'propanolol', 'tapentadol', 'esketamine', 'sine', 'isopropylphenidate', 'ethylphenidate', 'diphenhydramine', 'metodesnitazene',
 'fluonitazene', 'tiletamine', 'flubromzolam', 'isotonitazene', 'proppranolol', 'racetam', 'desoxymethoxetamine', 'imidazenil',
 'isopropyphenidate', 'propylphenidate', 'fluoromethylphenidate', 'lisdexamphetamine', 'isoproscaline',
 'isopropoxyphenethylamine', 'mhp', 'lisdexamfetamine', 'flourodeschloroketamine', 'sulbutiamine', 'trpytamine', 'methiopropamine', 'methalyescaline',
 'flurazepam', 'olanzapine', 'dizocilpine', 'nimetazepam', 'methylenedioxymethamphetamine', 'etonitazene',
 'lormetazepam', 'flunitrazepam', 'dxe', 'temazepam', 'oxazepam', 'ephinidine', 'thiamine', 'tryosine', 'bromozolam', 'isopropylphenidine',
 'chloroephenidine', 'hydroxymetamine', 'pcm', 'methoxyketamine', 'norketamine', 'cyclopropylmescaline', 'dichloromescaline', 'dibromomescaline', 'hodgkinsine',
 'phenazepam', 'brotizolam', 'hearthstone', 'methallallylescaline', 'deoxymethoxetamine', 'zolam', 'methoxpropamine',
 'metilphenidate', 'deschloroketamine','itonitazene']

additional_drug_terms = ['opioid','tramadol','tramadol','dopamin','vyvans','oxycodon','dsmt','gabapentin','memantin','benzo',
                         'opiat','kpin','psilocybin','fdck','mxipr','hexen','redos','arylcyclohexylamin','odsmt','methadon','dipt',
                        'morphin','etazen','eutylon','suboxon','glycol','mxpr','dmxe','shroom','isom','amphetamin','methylphenid','mapb',
                        'kratom','ethyl','coke','adderall','etiz','meth','heroin','mdma','cannabinoid','benzos','phenibut','ethanol','cathinone',
                        'cathinon','gram','ketamin']

misc_terms = ['researchchem','wiki','https','subreddit','psychonautwiki','clam','pyro','adhd','doses','didn',
              'don','stims','reddit','doesn','woudln','don','taper','honestly','solut','experience','effect','experi',
             'minut','peopl','daili','pretti','sleep','question','reddit',]


# In[15]:


additional_terms = set(drug_corpus_clean + additional_drug_terms + misc_terms)


# In[16]:


drug_corpus = set(drug_corpus_clean + additional_drug_terms)


# In[17]:


filtered2 = []
for i in data2.general_words_removed:
    new_data = i.split()
    post_filter = []
    for i in new_data:
        if len(i) > 4 and i not in additional_terms:
            post_filter.append(i)
    post_filter = ' '.join(post_filter)
    filtered2.append(post_filter)  
data2['drugsremoved'] = filtered2
data2 = data2.reset_index()


# In[18]:


tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                stop_words = 'english',
                                lowercase = True,
                                token_pattern = r'\b[a-zA-Z]{3,}\b',
                                max_df = 0.9, #ignore terms that appear in more than X% of the document 
                                min_df = 2)  #ignore terms that appear in less than X documents
dtm_tf = tf_vectorizer.fit_transform(data2.drugsremoved)


# In[19]:


tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
dtm_tfidf = tfidf_vectorizer.fit_transform(data2.drugsremoved)


# In[20]:


# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


# In[21]:


ex_label = [e[:30]+"..." for e in data2.drugsremoved]
doc_word = tf_vectorizer.fit_transform(data2.drugsremoved)
pd.DataFrame(doc_word.toarray(), index=ex_label, columns=tf_vectorizer.get_feature_names()).head(10).reset_index(drop=True, inplace=True)


# In[22]:


doc_topic = loaded_model.fit_transform(doc_word)


# In[23]:


topics = pd.DataFrame(doc_topic.round(5),
             index = ex_label,
             columns = ["Psycadelic","Euphoric",'Negative','Dangerous'])
#topics.reset_index()


# In[24]:


maxValueIndexObj = topics.idxmax(axis=1)
topics['effect'] = maxValueIndexObj
#topics = topics.reset_index()


# In[25]:


topics = topics.reset_index()


# In[26]:


a_file = open("drugs_corpus.csv", "r")
corpus1 = [s.strip() for s in a_file.readlines()]
drugs_corpus = set(corpus1)


# In[27]:


drug_terms = []
for i in data2.text:
    new_data = i.split()
    post_filter = []
    for i in new_data:
        if i in drugs_corpus:
            post_filter.append(i)
            #post_filter = remove_duplicate(post_filter)
    post_filter = ' '.join(post_filter)
    drug_terms.append(post_filter)
data2['drug_terms'] = drug_terms


# In[28]:


topics


# In[29]:


data2


# In[30]:


combined_df = pd.concat([topics, data2], axis=1)


# In[31]:


combined_df = combined_df.drop(['index', 'index','Psycadelic','Euphoric','Negative','Dangerous','split_text','counter','general_words_removed','drugsremoved'], axis=1)


# In[32]:


st.dataframe(combined_df)


# In[ ]:




