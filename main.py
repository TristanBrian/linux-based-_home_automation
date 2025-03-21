import logging
import time
import paho.mqtt.client as mqtt
import Adafruit_DHT
import RPi.GPIO as GPIO

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Sensor:
    def __init__(self, sensor_type, pin, mqtt_topic):
        try:
            self.client = mqtt.Client()
            self.client.connect("localhost")
        except Exception as e:
            logging.error(f"Failed to connect to MQTT broker: {e}")
            raise
    def __init__(self, sensor_type, pin, mqtt_topic):
        self.sensor_type = sensor_type
        self.pin = pin
        self.mqtt_topic = mqtt_topic
        self.client = mqtt.Client()
        self.client.connect("localhost")

    def read_data(self):
        try:
            raise NotImplementedError
        except Exception as e:
            logging.error(f"Error reading data from {self.sensor_type}: {e}")

class DHT22Sensor(Sensor):
    def __init__(self, pin, mqtt_topic):
        super().__init__("DHT22", pin, mqtt_topic)

    def read_data(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin)
            if humidity is not None and temperature is not None:
                self.client.publish(self.mqtt_topic, f"{temperature},{humidity}")
                logging.info(f"Published data: Temperature={temperature}°C, Humidity={humidity}%")
        except Exception as e:
            logging.error(f"Error reading DHT22 sensor data: {e}")

class PIRSensor(Sensor):
    def __init__(self, pin, mqtt_topic):
        super().__init__("PIR", pin, mqtt_topic)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read_data(self):
        try:
            if GPIO.input(self.pin):
                self.client.publish(self.mqtt_topic, "Motion Detected")
                logging.info("Motion detected")
        except Exception as e:
            logging.error(f"Error reading PIR sensor data: {e}")

if __name__ == "__main__":
    dht_sensor = DHT22Sensor(pin=4, mqtt_topic="home/sensor/temperature")
    pir_sensor = PIRSensor(pin=17, mqtt_topic="home/sensor/motion")

    while True:
        dht_sensor.read_data()
        pir_sensor.read_data()
        time.sleep(10)
