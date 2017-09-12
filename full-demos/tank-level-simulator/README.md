# Tank Level Simulator

This application is a simple end-to-end demonstration of ZumLink IPR programmability. It simulates monitoring of a oil or water tank using a level sensor (represented by a potentiometer), and indicates when a high or low threshold has been exceeded by illuminating LEDs. It will also publish sensor data to an MQTT broker. A second app will subscribe to the MQTT broker and chart the level data in a web page.

## Goal:

Demonstrate a distributed application consisting of two linked applications:

1. A Sensor app that:
    - Monitors a sensor
    - Transmits sensor data to a central location
    - Takes action when thresholds are exceeded
2. A Charting app that:
    - Receives sensor data
    - Displays sensor data in a web page


## Approach

Connect a potentiometer (simulating a tank level sensor) and two LEDs (for indicating exceeded thresholds) to a ZumIQ-enabled radio via an IOEX-4422 Serial Base.

Write a Sensor app on the radio that monitors tanks levels via Modbus polling of the Serial Base. If thresholds are exceeded, send Modbus commands to illuminate the threshold LEDs. Finally, transmit level sensor readings via MQTT.

Write a Charting app that receives level sensor reading and displays those readings on a web page.

**NOTE:** For simplicity and to focus on app development, both the Sensor and Charting apps will be run the same Z9-PE.

## Procedure

First, see [Hardware Setup](hardware-setup.md) to set up the components on a breadboard, and connect them to the Z9-PE using a IOE-4422 Serial Base.

Second, see [Software Prerequisites](software-prerequisites.md) to get the Z9-PE configured with Mosquitto and other dependencies.

Finally, see the [Python App](python/README.md) or [Node-RED App](node-red/README.md) for instructions on creating the Sensor and Charting apps.
