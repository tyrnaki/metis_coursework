# NYC Subway Station Recommendations for WomenTechWomenYes (WTWY)

*Walter Tyrna*

## Abstract

The goal of this project is to help WTWY identify which subway stations their street teams can target to spread awareness of their organization and identify individuals to attend their gala and donate to the organization. Using MTA turnstile data, I identified a preliminary list of subway stations that was further refined using economic data and geographic data. 

## Design
WTWY’s street teams aim to meaningfully engage with potential organization supporters - as a result, operating in an overly busy subway station would not provide an ideal environment. MTA subway data will inform not only station business as defined by cumulative entries and exits, but also station size by turnstile, yielding a list of “medium stations”. The data is scoped from 05/29/21 - 09/03/21 because vaccinations became more available during this period, making the data more reflective of pre-pandemic times. Zip code data will further refine the data, revealing which stations are located in higher income areas (to increase likelihood of donations). To complete the refining process, geographic data will consider which stations are located near universities as well as Whole Foods (WF) and Trader Joes (TJ), which acts as a proxy for locations with individuals with higher levels of education, probably open to WTWY’s mission. The top stations will include an analysis of best days to collect signatures. 

## Data
The MTA dataset contains 2918407 turnstile data entries across all NYC subway stations (472 stations). This data includes information regarding the number of turnstiles per station, entries, exits, and time series data. Zip code data from the census is made up of 181 rows of income data for zip codes within NYC in 2019. I used data points from Google Maps and NYCOpenData for store, university, and subway station locations. 

## Algorithms
1. Clean & aggregate MTA station data based on station ridership and station size.
2. Clean subway location data to merge geocoord information with MTA data.
3. Yield Zip Code data per station and match with economic data.
4. Map location data to determine which subway stations have WF, TJ, and universities within a half mile radius.
5. Produce visual analysis of time series data on top stations. 

## Tools
- SQL for data storage and access
- Pandas for data manipulation
- Matplotlib for plotting
- Fiona for KMZ (google map) data processing
- Geopy for querying geographic data
- Folium for interactive map

## Communication
Slides and visuals presented in class.
