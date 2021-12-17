# Engineering a New Psychoactive Substance (NPS) Monitoring Dashboard
Walter Tyrna

## Abstract
The goal of this project is to build upon the model created during the NLP module to create an interactive and regularly updating web application.

The web application aims to provide a user with quick charts and insights into substances discussed on the subreddit [Research Chemicals](https://www.reddit.com/r/researchchemicals/). This dashboard can help analysts, law enforcement, and policymakers covering synthetic drugs to quickly identify trends in aggregate text data.

## Design
This project uses both historic (up to one year ago) and current data pulled from the Research Chemicals subreddit. The [PushShift API](https://github.com/pushshift/api) provided data from mid-December 2020 to 2021, while the [Reddit API](https://www.reddit.com/dev/api/) provides daily subreddit information (through cron). The raw data is pulled and stored in [Mongo Atlas](https://www.mongodb.com/cloud), processed locally using a pre-trained Latent Dirichlet Allocation (LDA) model, then re-stored in Mongo Atlas. The post-processed data is then fed into a web app using [Streamlit](https://streamlit.io/).
  
The web app provides trends for the past year that a user can then down-select by a given timeframe. These trends include aggregate drug term counts by drug user expereince and by timeframe, links to more information about a given substance, and examples of the types of posts associated with the data. 

## Data
Each data point is a unique reddit post and its comments. The raw dataset of historic (one year) posts included over 80,000 posts. The number of preprocessed datapoints increases daily.

Post-processing - removing posts with less than 100 words - the corpus of historic posts dropped to over 10,000. 

To expand the corpus of stop words, I included a corpus of the [10,000 most common English words in order of frequency](https://github.com/first20hours/google-10000-english). 

## Algorithms
### Data Collection 
*Files: [Historic Data Pull](https://github.com/tyrnaki/metis_coursework/blob/1ae7a516013a10526c5dffdd99bdee68fdf4a227/engineering/final/Historic%20Reddit%20Pull.ipynb), [Historic Data Push to Mongo](https://github.com/tyrnaki/metis_coursework/blob/main/engineering/final/MongoDB%20Upload%20Historic%20Data.ipynb), [Daily Data Pull, Push to Mongo](https://github.com/tyrnaki/metis_coursework/blob/c4a315ced53570c081f823d64a9a612b21363582/engineering/final/Reddit_Daily_Pull.py)*

*Historic Data:*
1. Build function to determine unicode dates & build in sleep to avoid scrape time out.
2. Pull data from the PushShift API.
3. Export data to json.
4. Connect to MongoDB.
5. Export data to MongoDB.

*Daily Pull*
1. Connect to Reddit PRAW API.
2. Connect to MongoDB.
3. Pull most recent data from subreddit.
4. Export data to MongoDB.

### Corpus Cleaning, EDA, & Latent Dirichlet Allocation (LDA) Model Application 
*Files: [Historic Data](https://github.com/tyrnaki/metis_coursework/blob/1ae7a516013a10526c5dffdd99bdee68fdf4a227/engineering/final/Corpus_Cleaning_Tagging_Big_DataSet.ipynb), [Daily Data](https://github.com/tyrnaki/metis_coursework/blob/main/engineering/final/Corpus_Cleaning_Tagging_Regular_Data.py)*

* The larger dataset required more processing because it was too large for one entry into the database.
1. Connect to MongoDB and pull raw data
2. Remove posts less than 100 words.
3. Remove capital letters and punctuation from corpus.
4. Create new corpora of English stopwords.
5. Remove stopwords from corpus and stem text.
6. Iterate over text to determine additional drug terms for drug corpus. 
7. Remove drug related terms and other noise.
8. Apply tokenization
9. Upload pretrained LDA model & assign topics to each post
10. Apply drug corpus to text and topics dataframe to determine which drug types correspond to each topic
11. Make dataframes into dictionaries
12. Upload to MongoDB

### Create streamlit application files
*Files: [File Repo](https://github.com/tyrnaki/metis_coursework/tree/main/engineering/for_streamlit_app)*
1. Connect to MongoDB and pull post-processed data 
2. Create functions that correspond to application features
3. Create requirements.txt file
4. Connect streamlit to github repo

## Tools
- Requests, JSON, Reddit PRAW for API data aquisition
- Pandas for data manipulation
- Plotly for graphics
- NLTK for text manipulation  
- SKlearn for tokenization and model implementation
- Pickle for model reuse
- Datetime for timeseries data manipulation
- Pymongo to connect to Mongo Atlas
- Streamlit for app deployment

## Communication
Slides and visuals presented. [Live webapp](https://share.streamlit.io/tyrnaki/metis_coursework/main/engineering/for_streamlit_app/NPS_Dashboard.py) deployed.
