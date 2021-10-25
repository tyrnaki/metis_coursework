## Classification analysis of COVID-19 data

The goal of this project is to create a model that determines an individual's risk of contacting COVID-19 based on survey data collected by Imperial College of London (ICL). Since the ICL dataset was collected before vaccines were developed, the utility of this model is to determine which factors most drove risk for COVID-19 as a means to better respond to similar pandemics in the future. 

I focused the model on data from the United States from early Feburary through September 2020 (approx 34,000 rows) and initially included 29 rows of both numeric and categorial data that documented underlying health conditions, social conditions, and behaviors before contracting COVID-19. I aggregated some of these categories into overall scores. 

My baseline model consideres the target of "Have you tested positive for COVID-19? - Yes" with the following features:
- Coming into contact with someone who had tested positive for COVID-19 (categorical)
- Travel to area with high COVID-19 prevalence (categorical)
- Facemask use (categorcial)
- Handwashing habits (categorical)
- Use of public transit (categorical)
- Shopping frequency (categorical)
- Gender (categorical)
- Employment Status (categorcial)
- Weight (numeric)
- Age (numeric)
- Household Size (numeric)
- Attending Events Score (numeric score based on categorical responses to attending events)
- Preexisting Condition Score (numeric score based on categorical responses to having health conditions)

Given that the prevalence of positive COVID-19 cases is low in the dataset (see graphic below), I oversampled the positive cases to have an equal amount of positive and negative cases.

<img src="data-spread.png" alt="drawing" width="700"/>


The main metric by which I plan to assess this model is recall because the impact of missing a positive COVID-19 case is higher than misclassifying a negative case as a positive. 




The project goal is to be able to produce a predictive model that can estimate a given property's ultimate selling price. Given the MAE of this model, I need to further feature engineer to reduce the MAE to an acceptable level. 

