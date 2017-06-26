Python Demo
===========

This demo will use several Python libraries for reading modbus registers and communicating via MQTT.

The source code for each radio's application will be in the respective folders. "Sensor Client" is for the radio reading modbus registers and "Charting Client" is for the radio receiving and charting the sensor data.

Installation Scripts will contain a shell script for each client application. Running each script will take care of downloading all needed packages and providing the finished applications under /home/devuser/apps in the radios. If you are cloning this repo it is best to clone into /home/devuser.

Detailed explanations are provided for the Hardware setup and for the Software setup in the .rst files in this repo.
