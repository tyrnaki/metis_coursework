# COVID-19 Retrospective: Predicting COVID-19 and Lessons Learned
Walter Tyrna

## Abstract
The goal of this project is to create an interpretable classification model based on data from a [study conducted by the Imperial College of London (ICL)](https://github.com/YouGov-Data/covid-19-tracker) during the first year of the pandemic.

The model aims to predict COVID-19 cases using behavioral, demographic, and health data. As the data was collected before vaccines for COVID-19 became available, the utility of the model comes from its interpretability where it can shed light on which factors most determined COVID-19 cases. This information can help policymakers better understand how to better mitigate a similar pandemic in the future. 

## Design
The ICL study consisted of an extensive questoinnare with over 100 questions per person surveyed. I scoped the data to 16 categories that focus on an individual's behavior, demographic, and health data. 

I chose to primarily focus on a logistic model to achieve better interpretability; however, I did consider other models (knn and tree-based models) to ensure that the ultimate model for this project is achieving optimal results. As the target data is extremely unequal (fewer than 500 COVID-19 cases to nearly 35,000 negative cases), I employed both SMOTE and oversampling techniques to improve model performance. 

Recall and AUC score are the main metrics that I use to determine model success as the impact of incorrectly classiying a COVID-19 case is greater than a false positive (someone without COVID-19 testing positive). 

## Data
Each row in the ICL dataset consists of an individual's responses to the COVID-19 survey. Once I scoped the data, each row included the following features:

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
- Household Size (categorical - this improved model performance)
- Attended small events (categorical)
- Attended medium events (categorical)
- Attended large events (categorical)
- Hosted Guests (categorical)
- Preexisting Condition Score (numeric score based on categorical responses to having health conditions)

The the dataset that yielded the best performance and interpretability for this project consisted of 32060 rows and 31 columns. 

## Algorithms
*EDA*
1. Download USA datset from ICL Github
2. Select behavioral, demographic and health data. 
3. Create dummy variables for categorical features and aggregate variables.
4. Create seperate datasets for behavioral, health, and combined data. 

*Classification Model Exploration*
1. Upload datasets to "Classification Sandbox"
2. Determine target imbalance and adjust using sklearn.resample to upsample data where 0 and 1 have equal counts
3. Test upsampled data on KNN, Logistic Regression, Decision Tree, and Random Forest models.
4. Determine most effective dataset and model through recall and AUC scores (combined dataset with Logistic Regression wins).

*Logistic Regression Exploration*
1. Upload datasets to "Logistic Regression Sandbox"
2. Test different versions of the dataset through the following
- Test SMOTE and upsampled data across logistic regression models with different C values.
- Determine optimal C and data types based on recall and AUC scores.
3. Create graphic with key coefficients


## Tools
- Pandas for data manipulation
- SKlearn for model implementation
- Imblearn to address model imbalance
- Matplotlib for graphics

## Communication
Slides and visuals presented.
