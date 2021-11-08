## NLP analysis of Novel Psychoactive Substance (NPS) Subreddit

The goal of this project is to create general categories of drug user responses (for example: euphoria, pain, etc) based on different drug types discussed by redditors on the subreddit [Research Chemicals](https://www.reddit.com/r/researchchemicals/). This analysis will highlight which drug types among the largely unregulated NPS categories of drugs causes most harm to users, helping inform government drug policymakers. 

The scraped data is made up of 1031 posts of at least 100 words from Sept 2020 - Nov 2021. After text preprocessing, I was able to create a seperate corpus of drugs (over 120 drugs) discussed in the subreddit. EDA of the drugs and postings reveals that most drugs do not appear in all listings, and that certian drugs are more prevalent (see chart below). This EDA does not consider groupings of drug types - for example, etizolam and clonazolam are both benzodiazepines - I plan to create larger groupings of general drug types. 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/NPS/EDA-chart.png" alt="drawing" width="400"/>

An initial analysis of the text data using Latent Dirichlet Allocation revealed some trends:

- There does appear to be an assoication between benzodiazepines (benzos in graphic) and health risks such as addiction and hospitalization:
<img src="https://github.com/tyrnaki/metis_coursework/blob/main/NPS/Benzos.png" alt="drawing" width="800"/>


- Plant-based psychedelics (shrooms) appear to be more associated with less dangerous experiences:
<img src="https://github.com/tyrnaki/metis_coursework/blob/main/NPS/Shrooms.png" alt="drawing" width="800"/>


The LDA charts show that some stop words still need to be removed. I plan to further refine the categories of drugs as well as the text for analysis.
