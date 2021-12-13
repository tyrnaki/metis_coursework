## Dangerous Novel Synthetic Substance Tracker Dashboard

This project aims to create a regularly updating (daily) dashboard that highlights trends in the [Research Chemicals](https://www.reddit.com/r/researchchemicals/) subreddit. 

Though a combination of the Reddit and PushShift APIs, I was able to collect one year's worth of posts and comments from the Research Chemicals subreddit - nearly 76,000 posts. This will be augemented daily with new Reddit posts. The data has been stored in MongoDB and fed into my previous NLP workflow using LDA to categorize which posts and related drug types are typical of "dangerous" experiences. 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/engineering/images/Dangerous_Drugs_One-Year.png" alt="drawing" width="400" position='absolute' float='right'/>

I plan to export the results of my NLP analysis to a webapp using Streamlit. In order to create a regularly updating app, I will automate daily pulls from Reddit's API with a cron scheduler. 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/engineering/images/workflow.png" alt="drawing" width="600" position='absolute' float='right'/>
