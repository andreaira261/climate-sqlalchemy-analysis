# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Users/andreaaguilar/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurements = Base.classes.measurement
stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp_dict():
    recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()
    recent_date_dt = dt.datetime.strptime(recent_date[0], '%Y-%m-%d').date()
    year_ago = recent_date_dt - dt.timedelta(days=365)
    precipitation = session.query(measurements.date, measurements.prcp).\
        filter(measurements.date <= recent_date_dt).\
        filter(measurements.date >= year_ago).all()
    prcp_dict = {date: prcp for date, prcp in precipitation}
    return jsonify(prcp_dict)
    
@app.route("/api/v1.0/stations")
def stations_list():
   stationslist = session.query(stations.station).all()
   stationslist1 = list(np.ravel(stationslist))
   return jsonify(stationslist1)

@app.route("/api/v1.0/tobs")
def tobs_list():
    recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()
    recent_date_dt = dt.datetime.strptime(recent_date[0], '%Y-%m-%d').date()
    year_ago = recent_date_dt - dt.timedelta(days=365)
    most_active_temps = session.query(measurements.tobs).\
        filter(measurements.date <= recent_date_dt).\
        filter(measurements.date >= year_ago).\
        filter(measurements.station == 'USC00519281').all()
    temeperaturelist = list(np.ravel(most_active_temps))
    return jsonify(temeperaturelist)
    
if __name__ == '__main__':
    app.run(debug=True)