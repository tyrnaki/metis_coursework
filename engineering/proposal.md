### Emerging Harmful Substance Dashboard Proposal

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Synthetic drugs have increasingly driven [US overdose deaths](https://www.npr.org/2021/07/14/1016029270/drug-overdoses-killed-a-record-number-of-americans-in-2020-jumping-by-nearly-30) over the last five years. New types of synthetic substances often lead to [sharp upticks of overdoses](https://www.wusa9.com/article/news/local/dc/new-powerful-opioid-found-on-dc-streets/65-7f37d942-3660-419f-9eab-d9f12ec9ca80), often catching government and harm reduction officals by surprise. 

Purpose: This project aims to create a regularly updating dashboard (daily) that highlights synthetic drugs most associated with harmful effects as informed by reddit forums. This effort will build upon the [NLP analysis](https://github.com/tyrnaki/metis_coursework/blob/9616299f7cf475a0fcb597d6ec31473d3b4acf91/NPS/NPS_presentation-update.pdf) I conducted during the NLP module. 

Customers: Government policymakers and law enforcement.

#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

This project primarily will use forum posts from the [Research Chemicals](https://www.reddit.com/r/researchchemicals/) subreddit. Given the limitations of the Reddit API, historic posts (aka not current) will be scraped using the PushShift API; I will also use Reddit's API to pull up-to-date posts. The scrape will pull from at least the past six months of data. Each post captured will have at least 100 characters to ensure sufficient complexity, I will aim to have a corpus of at least 5000 posts. 


#### Tools:
* How do you intend to meet the tools requirement of the project? 

EDA: Pandas for data cleaning & exploration

Data Storage: MongoDB to store the data

NLP: NLP packages to preprocess and model data

Visualization: I plan to create a webapp with the results of my modeling; however, the specific webapp is tbd. 

* Are you planning in advance to need or use additional tools beyond those required?

Tbd
#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be a basic webapp that uses real-time (daily updates) that highlight drug types most associated with harmful effects. A more advanced project goal is a webapp that allows a user to see changes overtime. 
