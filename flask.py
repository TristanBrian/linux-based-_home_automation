from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app)
MQTT_BROKER = "localhost"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sensor_data", methods=["GET"])
def get_sensor_data():
    """ 
    Retrieves the latest sensor data from the MQTT broker 
    and returns it as JSON.
    """
    # Placeholder for actual sensor data retrieval logic
    return jsonify({"temperature": "22.5", "humidity": "60"})
def control_relay():
    state = request.json.get("state")
    client = mqtt.Client()
    client.connect(MQTT_BROKER)
    client.publish("home/relay/control", state)
    return jsonify({"status": "success", "state": state})

    # Subscribe to MQTT topics for real-time updates
    def on_message(client, userdata, message):
        # Handle incoming messages
        print(f"Received message: {message.payload.decode()} on topic: {message.topic}")

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER)
    client.subscribe("home/sensor/temperature")
    client.loop_start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
