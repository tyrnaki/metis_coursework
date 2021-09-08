### WomenTechWomenYes (WTWY) Project Proposal

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

The goal of this project is to support WTWY decisionmaking in placing their staff at NYC subway stations. These staff will directly engage with commuters to collect emails. Through effective placement, WTWY will be able to spread their message, gain attendees to their gala, and recruit new members to financially contribute to the organization. This analysis will provide WTWY with a list of subway stations that not only have adequate foot traffic throughout the day, but also meet the organizations target demographics. For the purposes of this study, I will assume that WTWY is seeking to engage individuals who are in the technology industry (or at least supportive of inclusivity in tech), have achieved higher levels of education, and who have the means to contribute to the cause (high-middle to high income individuals). 


#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

I plan to use MTA turnstyle data, which is available on the MTA's website, to understand which subway stations have higher levels of foottraffic. This data includes timeseries information, which will provide insights on which times of day a given station is busiest. The dataset also includes information on the number of turnstyles at a given station, which acts as a proxy for station size. Since WTWY's street team is limited in size, the organization needs to consider not only what time of day to place their staff, but also which stations size provide an effective venue for in-person engagement (engagement may be more difficult in Times Square, for example, versus a neighborhood stop). 
Besides MTA turnstyle data, I hope to incorporate geographic and demographic data to provide nuance to the subway station data. NYC Open Data has locations of colleges and universities in NYC - proximity to a subway station (1/4 mi) will likely improve WTWY's ability to reach individuals receptive to their cause. Additionally, income data available on data.cccnewyork.org can help inform which locations will improve WTWY's ability to reach individuals with the disposible income to attend and to contribute to their gala. To augment this income data, I will also consider the proximity of Whole Foods and Trader Joes (1/4 mi) from subway stations as shoppers in these stores tend to have higher levels of income and education. 
I do not plan to model for this project

#### Tools:
* How do you intend to meet the tools requirement of the project? 

I will use SQL to build databases from pulled data, Pandas to clean the data, and Matplotlib to display the data. 

* Are you planning in advance to need or use additional tools beyond those required?

I would like to use a mapping tool to display where the stations are in NYC. 

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be a list of ten stations that would best meet WTWY's street team's needs. The list will consider which stations are the busiest but manageable in size as well as fit demographic requirements (proximity to universities/higher income grocery stores, middle to high income neighborhoods). 
