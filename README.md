# SocialCops
Technical Challenge

Challenge 1: Agriculture Commodities, Prices & Seasons

Aim: Your team is working on building a variety of insight packs to measure key trends in the Agriculture sector in India. You are presented with a data set around Agriculture and your aim is to understand trends in APMC (Agricultural produce market committee)/mandi price & quantity arrival data for different commodities in Maharashtra.

Objective:
1.	Test and filter outliers.
2.	Understand price fluctuations accounting the seasonal effect
1.	Detect seasonality type (multiplicative or additive) for each cluster of APMC and commodities
2.	De-seasonalise prices for each commodity and APMC according to the detected seasonality type
3.	Compare prices in APMC/Mandi with MSP(Minimum Support Price)- raw and deseasonalised
4.	Flag set of APMC/mandis and commodities with highest price fluctuation across different commodities in each relevant season, and year.


Variable description:
•	msprice- Minimum Support Price
•	arrivals_in_qtl- Quantity arrival in market (in quintal)
•	min_price- Minimum price charged per quintal
•	max_price- Maximum price charged per quintal
•	modal_price- Mode (Average) price charged per quintal


# Methodology

The methodology followed for this assignment was to first check for missing values in the data, followed by identifying the outliers using a box plot for the target variable modal_price.

The box plot showed a large number of data points above the upper whisker, the outliers. 
The next step was to calculate the interquartile range (IQR), and then removing data points that were below Quartile1 - 1.5 * IQR and Quartile3 + 1.5 * IQR, which left 59896 data points from the original 62428 data points.(4.07% data omission is assumed to be acceptable) 

Next, the data set had to be convereted to a time series, so as to plot the seasonal plots of the modal_price.

Once that was done, time series plot of the first APMC in the dataset = Ahmednagar was plotted with respect to the modal_price, which was not very conclusive. 
Upon checking the frequency of the the APMC commodities, the top five APMC's which came up were:

Mumbai                    1538
Pune                      1513
Nagpur                    1340
Barshi                    1076
Jalgaon                   1055
Solapur                    984

Whereas the highest in the frequency in the commodities were as follows:
gram                     4115
wheat(husked)            4097
soybean                  3727
sorgum(jawar)            3716
pigeon pea (tur)         3477

# Analysis

Plotting the seasonality for each aggregated top 5 APMC and commodity's shows a cyclic movement in the prices across APMC's and commoditites, and no clear additive or multiplicative seasonality.

The movement of prices from April 2014 till December 2016 have 2 identical cycles of drops and rises, whcih can be accounted for the type of crop the commodity is; that is; rabi or kharif crop.

The trends in deasonalised plots of the commoditites depict movement of the prices that is distinct for each commodity.

Comparing MSPrice with Modal_Price by creating a merged dataset with aggregated monthly data and subsetting commodities based on the ones present in both yearly MSPrice data and monthly Modal_Price data gives us the following graphs:

https://github.com/theSaumya/SocialCops/blob/master/PriceVSCommodity.png
These graphs show that the modal price is on a scale that extends 12000 rupees per quintal whereas the MSPrice has a scale with the high value ending below 6000 rupees per quintal.
This shows that for the selected commom commodities, the minimum prices set by the Government are quite low and the prices at which the commoditites are being sold at mandi's and APMC's are skyrocketing. 

# Final results 
The price differences in the minimum price set by the Government and the actual price that the commoditites are sold for may be due to a few reasons, one of which can be that the transportation cost involved may be too high for select commoditites. 
Since this is an aggregation on the APMC, Commodity and Year level, it may not be the exact clear picture on the miniscule level, but it brings to light the price differences between the decided prices and the real prices. 

