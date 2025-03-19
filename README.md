# Linux-Based Smart Home Automation System

A professional, scalable, and modular smart home automation system built using Raspberry Pi, Python, Flask, and MQTT. This project includes a custom Linux kernel module, real-time sensor data collection, and a web-based dashboard.

## Features
- **Custom Kernel Module:** Efficient GPIO control with error handling and logging.
- **Real-Time Data Transmission:** MQTT for communication between devices.
- **Web Dashboard:** Flask-based dashboard with real-time updates using SocketIO.
- **Sensor Integration:** DHT22 (temperature/humidity) and PIR (motion) sensors.
- **Relay Control:** Control appliances using a relay module.
- **New Features:** (Add any recent updates or features here)

## Hardware Requirements
- Raspberry Pi 4
- DHT22 Sensor
- PIR Motion Sensor
- Relay Module
- Jumper Wires and Breadboard

## Software Requirements
- Raspbian OS
- Python 3.x
- Flask, Flask-SocketIO, paho-mqtt, RPi.GPIO, Adafruit_DHT
- Mosquitto MQTT Broker
- Grafana (for visualization)

## Setup Instructions
1. **Install Dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip mosquitto grafana
   pip3 install flask flask-socketio paho-mqtt RPi.GPIO Adafruit_DHT
   ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/TristanBrian/linux-based-home-automation
   cd linux-based-home-automation
   ```

3. **Compile and Load the Kernel Module:**
   ```bash
   make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
   sudo insmod gpio_module.ko
   ```

4. **Run the Python Scripts:**
   ```bash
   python3 sensor_script.py
   python3 relay_control.py
   ```

5. **Start the Flask App:**
   ```bash
   python3 app.py
   ```

6. **Access the Web Dashboard:**
   Open http://<raspberry-pi-ip>:5000 in your browser.

7. **Documentation**
   Kernel Module: docs/kernel_module.md

   Python Scripts: docs/python_scripts.md

   Flask App: docs/flask_app.md

8. **License**
   This project is licensed under the MIT License. See LICENSE for details.

9. **Contributing**
   Contributions are welcome! Please read CONTRIBUTING.md for details.

10. **Acknowledgments**
   Eclipse Mosquitto for MQTT.

   Adafruit for the DHT22 library.

   Flask and Grafana communities.
