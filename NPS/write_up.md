# Understanding New Psycoactive Substances: A NLP Approach
Walter Tyrna

## Abstract
The goal of this project is to use natural language processing techniques to understand drug user experiences with new psycoactive substances (NPS) and to pair NPS drug types with these topics.

The model aims to create general topics based on the subreddit [Research Chemicals](https://www.reddit.com/r/researchchemicals/). These general topics will be re-applied to the corpus to determine which drugs correspond to each topic. This information can inform policymakers on which NPS are more harmful than others, helping shape drug policy.

## Design
This project uses data scraped from the Research Chemicals subreddit (using the [PushShift API](https://github.com/pushshift/api)) because it is the main subreddit dedicated to NPS. The scrape collected the top posts from each week starting in September 2020 to November 2021. 

I chose Latent Dirichlet Allocation (LDA) as the main model for this project as the aim of this project is mostly exploratory. Since the corpus is made up of a variety of user experiences with many drug types, an unsupervised model using LDA is appropriate for determining how topics align within the corpus. Additionally, LDA tools such as pyLDAvis help determine key words that make up each topic.   

## Data
Each data point in this project is a unique reddit post with at least 100 words. 

To expand the corpus of stop words, I included a corpus of the [10,000 most common English words in order of frequency](https://github.com/first20hours/google-10000-english). 

## Algorithms
*Data Collection* (clean)
1. Pull data from the PushShift API.
2. Build function to determine unicode dates & build in sleep to avoid scrape time out.
3. Scope posts to only include those with 100 words.
4. Export data to csv.

*Corpus Cleaning & EDA* (clean, sandbox1, sandbox2)
1. Remove capital letters and punctuation from corpus.
2. Create new corpora of English stopwords.
3. Remove stopwords from corpus and stem text.
4. Iterate over text to determine additional drug terms for drug corpus. 
5. Remove drug related terms and other noise.
6. Export data to csv.

*Latent Dirichlet Allocation (LDA) & EDA* (clean)
1. Upload dataset and apply tokenization
2. Use pyLDAvis to examine and adjust parameters (min_df, max_df, number of topics)
3. Once topics cohesive, assign topic names
4. Reassign topics to original text
5. Apply drug corpus to text and topics dataframe to determine which drug types correspond to each topic

## Tools
- Requests and JSON for API data aquisition
- Pandas for data manipulation
- Matplotlib for graphics
- NLTK for text manipulation  
- SKlearn for tokenization and model implementation

## Communication
Slides and visuals presented.
