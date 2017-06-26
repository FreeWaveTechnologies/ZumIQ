These two folder are the two client applications for the Python MQTT demo.

Sensor Client is for the radio connected to a serial base and sensors. This is the same radio where Mosquitto broker will run.

Charting Client will run on a separate radio not connected to sensors. It will use MQTT to talk to the Sensor Client radio, get its
sensor data, and chart it in a Flask/JS web app.

The troubleshooting folders in each of the two apps contain small scripts to check individual parts of each app for debugging purposes.
