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

session = Session(engine)

conn = engine.connect()

# App setup
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page. Here is a list of available endpoints:<br><br><br>Precipitation data: /api/v1.0/precipitation<br><br>Station data: /api/v1.0/stations<br><br>Temperatures of most active station: /api/v1.0/tobs<br><br>Min, max, and avg temperatures from selected date: /api/v1.0/[date]<br><br>Min, max, and avg temperatures from selected date range: /api/v1.0/[start date]/[end date]"

# @app.route("/api/v1.0/precipitation")

# @app.route("/api/v1.0/stations")

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)