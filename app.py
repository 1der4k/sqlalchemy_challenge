# Dependencies
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# DB setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# App setup
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page. Here is a list of available endpoints:<br><br><br>Precipitation data: /api/v1.0/precipitation<br><br>Station data: /api/v1.0/stations<br><br>Temperatures of most active station: /api/v1.0/tobs<br><br>Min, max, and avg temperatures from selected date: /api/v1.0/[date]<br><br>Min, max, and avg temperatures from selected date range: /api/v1.0/[start date]/[end date]"

@app.route("/api/v1.0/precipitation")
def prec_handler():
    session = Session(engine)
    query_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    meas_data = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= query_date).order_by(Measurement.date).all()
    results = []

    for row in meas_data:
        results.append({row[0]:row[1]})

    session.close()

    return jsonify(results)

@app.route("/api/v1.0/stations")
def station_handler():
    session = Session(engine)
    query_stations = session.query(Station.elevation,Station.longitude,Station.name,Station.id,Station.latitude,Station.station).all()
    results = []

    for row in query_stations:
        results.append({
            "elevation" : row[0],
            "longitude": row[1],
            "name": row[2],
            "id": row[3],
            "latitude": row[4],
            "station": row[5]
        })

    session.close()

    return jsonify(results) 

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)