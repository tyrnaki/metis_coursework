### Unsupervised Learning Analysis of Novel Psychoactive Substances (NPS)

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Synthetic drugs have increasingly driven US overdose deaths over the last five years. Fentanyl and methampetamines are the main drug types leading to overdoses but Novel Psychoactive Substances (NPS) have also caused an increasing share of overdoses. NPS, as compared to fentanyl or methampetamines, are made up of a large vareity of unregulated substances that US government policymakers and law enforcement struggle to keep track of until they already present an issue. 

Purpose: This analysis aims to use natural language processing modeling techniques to highlight which NPS are used by posters on the reddit group "Research Chemicals" and to determine which substances have the most detrimental effects on users. This information can help highlight emerging trends in drug use as warning to US government policymakers.

Customers: Government policymakers and law enforcement.

#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

This project primarily will use forum posts scraped from the Research Chemicals subreddit. The scrape pulls the top 100 posts per week from 2021 and 2020, the corpus will be made up of 1000+ posts with at least 100 words. 


#### Tools:
* How do you intend to meet the tools requirement of the project? 

EDA: Pandas to clean & explore the data
NLP: NLP packages to preprocess and model data

* Are you planning in advance to need or use additional tools beyond those required?

I plan to create visualizations based on the results, but the tools are still TBD.

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be an unsupervised learning model that is able to highlight which NPS are most mentioned during the web scrape timeframe. Further analysis will include user impact of drug use. 
