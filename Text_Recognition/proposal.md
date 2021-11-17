### Scraping Information from Illicit Advertisements using Deep Learning

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Many of the chemicals used to create synthetic drugs such as fentanyl and methamphetamine are openly advertised online by chemical distributors (largely in China). These distributors often try to evade chemical regulations and subsequent online marketplace regulations in China and the United States through advertisements using terms and spellings that are not easily machine readable, as well as through embedding contact and product information in images. 

Purpose: This project aims to use deep learning to recognize and extract text from images. This will help analysts looking at open source commerical data more quickly collect and connect data associated with illicit chemical distributors, in turn supporting investigations. 

Customers: Government analyists.

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
