from flask import Flask, jsonify
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()


@app.route("/")
def index():
    return jsonify({
        "temperature_humidity": sense.get_temperature_from_humidity(),
        "temperature_pressure": sense.get_temperature_from_pressure(),
        "pressure": sense.get_pressure(),
        "humidity": sense.get_humidity(),
    })


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
