from flask import Flask, jsonify

app = Flask(__name__)

# endpoint_list = [
#     {"endpoint" : "/api/v1.0/precipitation",
#     "description": "precipitation data"
#     },
#     {"endpoint" : "/api/v1.0/stations",
#     "description": "station data"
#     },
#     {"endpoint" : "/api/v1.0/tobs",
#     "description": "temperature observations of most active station"
#     },
#     {"endpoint" : "/api/v1.0/<start>",
#     "description": "minimum, maximum, and average temperatures from this date"
#     },
#     {"endpoint" : "/api/v1.0/<start>/<end>",
#     "description": "minimum, maximum, and average temperatures from this date range"
#     }
# ]

@app.route("/")
def home():
    return "Welcome to the home page. Here is a list of available endpoints:<br><br><br>Precipitation data: /api/v1.0/precipitation<br><br>Station data: /api/v1.0/stations<br><br>Temperatures of most active station: /api/v1.0/tobs<br><br>Min, max, and avg temperatures from selected date: /api/v1.0/<start><br><br>Min, max, and avg temperatures from selected date range: /api/v1.0/<start>/<end>"

# @app.route("/api/v1.0/precipitation")

# @app.route("/api/v1.0/stations")

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)