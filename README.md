# Machine Learning Final Project 

In this project, we will be using a Linear Regression Neural Network to predict the amount of bike riders using Toronto's Bike Share program. . We will do this using 3 inputs: Mean Temperature of that day, Total Precipitation, and Snow on the ground.(Subject to change). We used data from January 2022 to September 2024. The datasets were accessed using the links below: 

* https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/
* https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2002-06-04%7C2025-11-04&dlyRange=2002-06-04%7C2025-11-04&mlyRange=2003-07-01%7C2006-12-01&StationID=31688&Prov=ON&urlExtension=_e.html&searchType=stnProx&optLimit=yearRange&Month=1&Day=1&StartYear=2020&EndYear=2025&Year=2024&selRowPerPage=25&Line=0&txtRadius=25&optProxType=city&selCity=43%7C39%7C79%7C23%7CToronto&selPark&txtCentralLatDeg&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongDeg&txtCentralLongMin=0&txtCentralLongSec=0&txtLatDecDeg&txtLongDecDeg&timeframe=2&time=LST

Our first step was to obtain the data needed from these datasets. The code used for this can be found in the `CleaningDataset.ipynb` file. The output file is `combined_cleaned.csv`
