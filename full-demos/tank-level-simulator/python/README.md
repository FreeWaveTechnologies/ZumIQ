# Python Tank Level Monitoring Simulator

## Application Overview

The application has three components:

1. The Sensor Client app that:
    - Reads the potentiometer value using Modbus.
    - Illuminates LEDs indicating exceeded thresholds using Modbus.
    - Publishes the sensor data using MQTT.

2. The Mosquitto MQTT broker

3. The Charting Client app that:
    - Subscribes to the sensor data topic using MQTT.
    - Displays the sensor value and history in a web page.

In this demo, all apps are run on the same ZumIQ-enabled device for simplicity. Each could be run on different radios if desired, by changing the IP address of the Mosquitto broker in the two Client applications.

## Installation

The easiest way to get the apps running on a radio is to clone the Git repository and run the installation scripts included.

1. Login to the Z9-PE as "devuser" (See [Logging In](https://github.com/FreeWaveTechnologies/ZumIQ/wiki/Logging-In) for details)

2. Clone the git repo with the demo code:
```bash
    git clone https://github.com/FreeWaveTechnologies/ZumIQ.git
```
3. Install Mosquitto using the built-in script:

    install-mosquitto.sh

4. Run the demo script installers:
```bash
    cd ZumIQ/full-demos/tank-level-simulator/python/installation-scripts
    ./sensor-client-install.sh
    ./charting-client-install.sh
```
5. Rotate the potentiometer between its limits. One LED should illuminate near one limit, and the other LED should illuminate at the other limit.

6. Open a browser to http://192.168.111.100:5000. You should see the potentiometer value update in real time.



    
