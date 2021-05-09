from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page."

# @app.route("/api/v1.0/precipitation")

# @app.route("/api/v1.0/stations")

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)