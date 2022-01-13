# SQLAlchemy

## Surf's Up! 

![image](https://user-images.githubusercontent.com/86257908/132930303-78341446-e959-4425-b076-7250eb85c61b.png)

### Climate Analysis and Exploration 

#### Precipitation Analysis

* Find the most recent date in the data set.
* Retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.

![prcp](https://github.com/abednarz210/sqlalchemy-challenge/blob/main/PrcpDF.png)


### Station Analysis


* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations (i.e. which stations have the most rows?).
* List the stations and observation counts in descending order.
* Which station id has the highest number of observations?
* Using the most active station id, calculate the lowest, highest, and average temperature.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filter by the station with the highest number of observations.
* Query the last 12 months of temperature observation data for this station.
* Plot the results as a histogram with bins=12.

![temp_hist](https://github.com/abednarz210/sqlalchemy-challenge/blob/main/tempOBS.png)

