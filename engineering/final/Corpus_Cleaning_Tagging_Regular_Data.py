#!/usr/bin/env python
# coding: utf-8

# In[21]:


import nltk
import pandas as pd
import matplotlib as plt
import re
import string
from pprint import pprint
from jsonmerge import merge

import pickle
import plotly

import pymongo
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, WordNetLemmatizer

from warnings import filterwarnings
filterwarnings('ignore')


# In[17]:


client = pymongo.MongoClient("mongodb+srv://wtyrna13:WkuLFvYJ7rUHQXu@cluster0.tpw7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.new_scrapes


# In[18]:


db.collection_names()


# In[22]:


cursor = db.reddit_data.find()
all_data = list(cursor)


# In[70]:


data_for_processing = all_data[-1]


# In[72]:


big_df1 = pd.DataFrame([data_for_processing])


data = big_df1.T # or df1.transpose()


# In[73]:


data


# In[27]:


data.rename(columns={ data.columns[0]: "text" }, inplace = True)


# In[28]:


data


# In[29]:


split_text = []
for i in data.text:
    text = str(i).split()
    split_text.append(text)


# In[30]:


data['split_text'] = split_text


# In[31]:


counter = []
for i in data.split_text:
    counter.append(len(i))


# In[32]:


data['counter'] = counter


# In[33]:


mask = (data['counter'] > 100)


# In[34]:


data2 = data[mask]


# In[35]:


data2


# In[36]:


#### make lowercase and remove punctuation

alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())

data2['text'] = data2.text.map(alphanumeric).map(punc_lower)


# In[37]:


def make_corpus(x):
    a_file = open(x, "r")
    corpus = [s.strip() for s in a_file.readlines()]
    a_file.close()
    return corpus


# In[38]:


corpus1 = make_corpus('stop_words_english.txt')
corpus2 = make_corpus("google-10000-english-usa.txt")
big_corpus = corpus1 + corpus2


# In[39]:


stemmer = SnowballStemmer('english')


# In[40]:


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


# In[41]:


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


# In[42]:


additional_terms = set(drug_corpus_clean + additional_drug_terms + misc_terms)


# In[43]:


drug_corpus = set(drug_corpus_clean + additional_drug_terms)


# In[44]:


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


# In[45]:


data = data2


# In[46]:


tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                stop_words = 'english',
                                lowercase = True,
                                token_pattern = r'\b[a-zA-Z]{3,}\b',
                                max_df = 4, #ignore terms that appear in more than X% of the document 
                                min_df = 0)  #ignore terms that appear in less than X documents
dtm_tf = tf_vectorizer.fit_transform(data.drugsremoved)


# In[47]:


tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
dtm_tfidf = tfidf_vectorizer.fit_transform(data.drugsremoved)


# In[48]:


# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


# In[49]:


ex_label = [e[:30]+"..." for e in data.drugsremoved]
doc_word = tf_vectorizer.fit_transform(data.drugsremoved)
pd.DataFrame(doc_word.toarray(), index=ex_label, columns=tf_vectorizer.get_feature_names()).head(10).reset_index(drop=True, inplace=True)


# In[50]:


doc_topic = loaded_model.fit_transform(doc_word)


# In[51]:


topics = pd.DataFrame(doc_topic.round(5),
             index = ex_label,
             columns = ["Psycadelic","Euphoric",'Negative','Dangerous'])


# In[52]:


maxValueIndexObj = topics.idxmax(axis=1)
topics['effect'] = maxValueIndexObj
topics = topics.reset_index()


# In[53]:


data


# In[54]:


effects = []
for i in topics.effect:
    effects.append(i)
data['effect'] = effects


# In[55]:


data


# In[56]:


from collections import OrderedDict
def remove_duplicate(s): 
    new_list = []
    i = ",".join(OrderedDict.fromkeys(s))
    i = i.split(',')
    for i in i:
        new_list.append(i.replace('"', ""))
    return new_list 


# In[59]:


drug_terms = []
for i in data.text:
    new_data = i.split()
    post_filter = []
    for i in new_data:
        if i in drug_corpus:
            post_filter.append(i)
            post_filter= remove_duplicate(post_filter)
    post_filter = ' '.join(post_filter)
    drug_terms.append(post_filter)


# In[60]:


drug_terms


# In[61]:


data['drugs_in_text'] = drug_terms


# In[62]:


to_database = data.drop(['split_text','counter','general_words_removed','drugsremoved'], axis=1)


# In[63]:


to_database_dict = to_database.to_dict()


# In[64]:


to_database_dict


# In[65]:


db = client.for_class


# In[66]:


db.collection_names()


# In[68]:


result=db.for_class.cleaned_data.insert_one(to_database_dict)









