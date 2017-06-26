This directory contains all source code for an end to end application written out in Python as well as Node-RED.

The Python demo contains two applications:

One is for the ZumLink IPR collecting sensor information from a serial base and publishing it to Mosquitto broker running in the radio itself. 

The other application is for a radio that communicates with the first radio's MQTT broker, asking for the sensor information and sending it 
through a Flask/JS website app to chart the data in real time.

The Node-RED demo contains flows which can be copy pasted into the Node-RED GUI to replicate app. There are two apps, just like for Python, one for the radio collecting sensor information and sending it to the broker, and one for asking the broker for the sensor info and charting it in Node-RED. 
One important difference is that the Mosquitto broker for the Node-RED apps will run in the radio that charts data instead of the radio collecting sensor information. This shows that the MQTT broker can run anywhere as long as clients are correctly pointing to it.

There are troubleshooting folders to test smaller parts of the applications individually, this is to help debugging issues.
