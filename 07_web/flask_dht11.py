from flask import Flask, render_template
import Adafruit_DHT
import json

sensor = Adafruit_DHT.DHT11 #dht2 도 있음
DHT_PIN = 3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dht11.html")

@app.route("/monitor")
def monitoring():
    h, t= Adafruit_DHT.read_retry(sensor, DHT_PIN)
    if h is not None and t is not None:
        data = {'humidity': h, 'temperature': t}
        return json.dumps(data)
    else:
        'Read error'

if __name__ == "__main__":
    app.run(host="0.0.0.0")