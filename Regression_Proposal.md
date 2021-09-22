### Regression Analysis of DC Real Estate Market Proposal

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Throughout the pandemic, major cities across the US have expereinced a real estate price boom where many sellers have been able to exeed their asking price by well over $100k and have been able to sell homes within short offering windows. However, this price increase has typically coencided with single family homes, and not condominum units. 

Purpose: This regression analysis plans to predict potential increase or decrease in a given home sale price. In other words, can a seller expect an increase or decrease, and by how much, in the home's final sale price as compared to the original asking price.

Customers: This regression would benefit homesellers or developers looking to take advantage of increased real estate demand. 


#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

This project primarily will use data scraped from Compass Real Estate's website. Compass is one of the top real estate companies in Washington DC and its website pulls the same data as other national real estate websites (such as Zillow). I would like to integrate further geographic-based data (such as crime, or income level in a given area) but I have not determined those data sources, yet.

The individual sample for this project will be a property sold in the DC area in the past two years. For each property, I will consider the following features, at a minimum:
- Number of baths
- Number of beds
- SQFT
- Lot size
- Type of property (condo or house)
- Does it have a garage 
- Does it have backyard (or outdoor space)
- Is it a new construction?
- How many days was it on the market?
- Asking price
- Sold price
- Difference between asking & sold

The target for this model will be the potential deviation from a given property's asking price.

#### Tools:
* How do you intend to meet the tools requirement of the project? 

I will use Beautifulsoup to scrape data from Compass' website, Pandas to clean the data, and sklearn to conduct a linear regression. 

* Are you planning in advance to need or use additional tools beyond those required?

I would like to use geopy to add geographic data to the regression as well as folium to display pricing data on a map of Washington DC (as a heat map). 

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be a regression that consideres the features I outline above that provides reasonable predicitions for real estate sales. 
