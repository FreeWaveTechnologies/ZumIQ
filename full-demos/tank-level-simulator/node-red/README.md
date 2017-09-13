# Node-RED Tank Level Monitoring Simulator

## Application Overview

The application has three components:

1. The Sensor Client flow that:
    - Reads the potentiometer value using Modbus.
    - Illuminates LEDs indicating exceeded thresholds using Modbus.
    - Publishes the sensor data using MQTT.

2. The Mosquitto MQTT broker

3. The Charting Client flow that:
    - Subscribes to the sensor data topic using MQTT.
    - Displays the sensor value and history in a web page.

In this demo, all apps are run on the same ZumIQ-enabled device for simplicity. Each could be run on different radios if desired, by changing the IP address of the Mosquitto broker in the two Client applications.

## Installation

The Node-RED demo can be set up using built-in scripts on the ZumIQ-enabled Z9-P Series device.

1. Login to the ZumIQ-enabled device as "devuser" (See [Logging In](https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/Logging-In) for details)

2. Set the date (this can be skipped if NTP is already configured):
```bash
    setdate.sh
```
3. Install the Mosquitto service:
```bash
    install-mosquitto.sh
```
4. Install the Node-RED service:
```bash
    install-node-red.sh
```
5. Install the Node and Node-RED support modules (includes components such as Serial and Modbus support):
```bash
    install-npm-modules.sh
```
6. Once the script completes, wait 30 seconds to allow the serivces to start up. Then, open a web browser to `http://192.168.111.100:1880` (use the IP address of your device if different).

7. From the menu in the upper-right corner of the Node-RED webpage, select Import > Clipboard.

8. Copy the contents of "sensor-client.json" into the pop-up windows.

9. Select "new flow", and "Import"

10. Repeat steps 6-8, but for "charting-client.json".

11. Click the red "Deploy" button to apply the flows to the service.

12. Rotate the potentiometer between its limits. One LED should illuminate near one limit, and the other LED should illuminate at the other limit.

13. Open a browser to http://192.168.111.100:1880/ui. You should see the potentiometer value update in real time.






    
