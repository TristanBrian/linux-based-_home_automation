from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app)
MQTT_BROKER = "localhost"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control", methods=["POST"])
def control_relay():
    state = request.json.get("state")
    client = mqtt.Client()
    client.connect(MQTT_BROKER)
    client.publish("home/relay/control", state)
    return jsonify({"status": "success", "state": state})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)