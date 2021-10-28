# COVID-19 Retrospective: Predicting COVID-19 and Lessons Learned
Walter Tyrna

## Abstract
The goal of this project is to create an interpretable classification model based on data from a study conducted by the Imperial College of London during the first year of the pandemic.

The model aims to predict COVID-19 cases by behavioral, health, and demographic data. As the data was collected before vaccines for COVID-19 became available, the
I used monthly ridership data from [CaBi's website](https://www.capitalbikeshare.com/system-data) and augmented it with location data from [DC Open Data](https://opendata.dc.gov/datasets/neighborhood-clusters/explore) and Geopy

## Design
This project considered aggregate ridership data for each dock in CaBi's network. I specifically focused on "start_ride" as a proxy for the number of bicycles available at a given dock (as rides cannot start without a bike present). This project looks at ridership from both a station and a neighborhood level, as individuals would usually consider several bikeshare docks within their given area. 

Bicycle availablity at both a neighborhood and dock level allows CaBi to determine if a given area doesn't have enough bicycles, or if a specific dock needs maintenence.

## Data
The dataset from CaBi's website is made up of individual ride data to include 'start station', 'end station', times, and coordinates, aggregated during monthly intervals (12 columns per sheet, each sheet with at least 300,000 rows). 

After cleaning and aggegating the data in python, the csv used in my analysis includes timeseries data for 656 bikeshare docks (columns with two years worth of data, at a month-level), as well as columns indicating coordinate, zipcode, and neighborhood (21 columns, 656 rows).

## Algorithms
*Aggregation of Bikeshare Ride Data - Python*
1. Combine monthly ride-level data (over ten csv's)
2. Aggregate the data to determine rides began per station per month
3. Export aggregated csv to Google Sheets

*Determine Bikeshare Location data - Python*
1. Use bikeshare dock coordinate locations with geopy to determine zipcodes for each station
2. Upload shape files of DC neighborhoods, check if dock coordinate in neighborhood to determine neighborhood where applicable
3. Export location csv to Google Sheets

*EDA in Google Sheets*
1.  Upload and combine Bikeshare Ride and Location data into Google Sheets
2.  Compare ridership trends per dock on a month-to-month and year-to-year level
3.  Compare ridership trends per neighborhood on a month-to-month and year-to-year level
4.  Determine when docks became introduced in the system
5.  Create graphics based on above
6.  Export csv's based on above to Tableau

*EDA in Tableau*
1. Upload csv's of ridership changes over time into Tableau 
2. Create maps based on data

## Tools
- Pandas for data manipulation
- Geopy, JSON, and Shapely for data geographic information
- TQDM for function validation
- Google Sheets for EDA and visualizations
- Tableau for EDS and visualizations

## Communication
Slides and visuals (slide deck and [tableau dashboard](https://public.tableau.com/app/profile/walter.tyrna/viz/ChangesinCaBiRidershipsummer20-21/Dashboard1)) presented.
