### Classification Analysis of COVID-19 Cases

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Throughout the pandemic, governments worldwide provided oftentimes uneven guidance on how to protect oneself from COVID-19, leading to public confusion and frustration.  Imperial College London, in order to better understand the virus' spread, [conducted a worldwide study](https://github.com/YouGov-Data/covid-19-tracker) of not only symptoms and demographics but also behaviors of individuals that tested positive for COVID-19. The majority of the survey's data was collected before widespread vaccine availability. 

Purpose: The purpose of this classification model is to better understand behaviors and demographics (age, gender, etc) that correlated to contracting COVID-19.

Customers: This study would benefit public health officials interested in applying lessons learned from the COVID-19 pandemic to future pandemics.  


#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

This project primarily will use data from Imperial College London's COVID-19 study. The study was conducted at a [country level](https://github.com/YouGov-Data/covid-19-tracker/tree/master/data), with data for each country consisting of at least 30,000 rows and 40 columns. 

I plan to scope this study to data from the United States, taken from April to September 2020. An individual sample is an person interviewed for the study. For each individual, I will consider the following features (behaviors, health aspects, and demographics) at a minimum:
- Contact with individuals positive for COVID-19
- Travel 
- Mask usage
- Use of soap/handwashing
- Going out into public
- Attending social gatherings
- Going to shops
- Weight
- Age
- Gender
- Household size
- Employment status

The target for this classification model is whether or not an individual contracted COVID-19. The goal of this study is to provide interpretable results to determine which features or combination of features best determined the target value. 

#### Tools:
* How do you intend to meet the tools requirement of the project? 

EDA: Pandas to clean & explore the data
Classification: sklearn to create a classifcation model (probably using random forest/decision tree). 

* Are you planning in advance to need or use additional tools beyond those required?

TBD

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be a classification model that is able to somewhat accurately predict whether or not a person contracted COVID-19 based on the features outlined above. A more finished product would yeild a higher accuracy. 
