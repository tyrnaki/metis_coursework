# DC Bikeshare Expansion and Customer Retention

## Backstory & Problem: 

Capital Bikeshare has expanded the number of stations in the DC area over the past year; however the expansion of stations seems to have outpaced bike availability, leading to more empty stations and frustrating existing customers. 

How can Captial Bikeshare broaden the number of stations in the DC area while maintaining bike service to preexisting customers?

By comparing bicycle movement and availablity before and after dock expansion, Captial Bikeshare can better allocate the number of bikes across both old and new bicycle docks. This helps keep old customers while attracting new memberships.

## Data Description: 

Capital Bikeshare's website (https://www.capitalbikeshare.com/system-data) provides data on all bikeshare rides on a monthly and yearly basis. Each row of data includes trip start & end times/locations. This data can provide timeseries information on which stations are busiest during given periods, as well as differences system-wide as new stations were introduced.

I will overlay this with additional datasets (tbd) from DC Open Data (https://opendata.dc.gov/). Data includes demographic information such as income in a given area.

This project does not include any modeling

## Tools:

I will use Excel/Google Sheets and Tableau to clean, explore, aggregate, and visualize the data. Given the size of sheets available from Capital Bikeshare, preliminary EDA will take place using Python (mostly Pandas).

## MVP:

An MVP for this project would be a comparison of the busiest bike docks before and after Captial Bikeshare's dock expansion.

