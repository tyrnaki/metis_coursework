## Analysis of the Washington DC Real Estate market

The goal of this project is to understand which factors most drive real estate sales prices in the DC area. To scope the data, this analysis only looks at single family homes and townhomes within 25 mi of downtown DC. 

![](mvp_figure.png)

I scraped data from Compass (a real estate company) to collect 2445 rows of data. This data was reduced to 909 rows once scoped for property type and distance from downtown (using geopy).

In addition to data scraped from Compass, I used a scrape from Washington DC's metro site and geopy to determine each property's distance from a subway station. 

To account for general locations, I grouped property zipcodes according to general geographic areas. 

My baseline model consideres the target of "Final Sale Price" with the following features:
- regions_DC West of River
- Property Age
- Beds
- Baths
- Stories
- Lot_Size
- Has_Garage_Yes
- distance_from_metro

Using a Lasso Regression on the above features, I achieved an R^2 of 0.4534 and an MAE of $212,193. The figure shows

To start exploring this goal, I used a linear regression model with one feature to describe Box Office Total Domestic Gross as a function of the Budget of a Movie.

The figure depicts the model (red) plotted against the actual data points. The prediction interval is plotted in green.

This result suggests that budget may have a significant positive impact on a film's revenue. However, the magnitude of the model's residuals makes it clear that budget is not the only important factor in determining the success of a film.
