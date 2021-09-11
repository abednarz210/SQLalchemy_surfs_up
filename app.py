import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, create_session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create_session
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    #last year precipitation
    session = Session(engine)

# Find the most recent date in the data set.
recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
# Starting from the most recent data point in the database. 
# Calculate the date one year from the last date in data set.

query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
recent_date = dt.date(2017, 8, 23)

# Perform a query to retrieve the data and precipitation scores

prcp_scores = (
    session.query(measurement.date, measurement.prcp).filter(measurement.date >= query_date)
    .order_by(measurement.date)
    return jsonify(prcp_scores)
    
    session.close()

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session 
    session = Session(engine)
most_active = (
    session.query(measurement.station, station.name,func.count(measurement.station)).\
    filter(measurement.station == station.station).group_by(measurement.station)
    .order_by(func.count(measurement.id).desc()).all()
)
station_id = most_active[0][0]
station_id_most = most_active[0][2]

#calculate lowest, highest, avg temp
most_active = ( 
    session.query(
    func.min(measurement.tobs),
    func.max(measurement.tobs),
    func.avg(measurement.tobs),
)   
.filter(measurement.station == most_active[0][0]).all()
)

    return jsonify(most_active)
session.close()

@app.route("/api/v1.0/stations")
def stations():
temp_obs = session.query(measurement.tobs).\
    filter(measurement.station == station_id).filter(measurement.date >= query_date).all()

temp_obs_df = pd.DataFrame(temp_obs, columns=['tobs'])
temp_obs_df.head()

    return jsonify(temp_obs)
    session.close()

    
    #####@app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return 

if __name__ == '__main__':
    app.run(debug=True)

