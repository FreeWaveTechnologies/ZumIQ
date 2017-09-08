Before running the install scripts for SENSORS CLIENT and CHARTING CLIENT applications there are a few things that need to be set:

1) The radio device must have an internet connection, otherwise software packages will not download.

2) The date for the device must be set to current UTC, otherwise software packages may not download properly.

3) The SENSORS CLIENT script is for the radio connected to the sensors/breadboard setup. The CHARTING CLIENT 
script will be the radio that receives the sensor info and displays live sensor data on a browser.

4) These installation scripts point to the code contained in folders "Sensor Client Python MQTT demo" and "Charting Client 
Python MQTT demo". Changing the source code locations will break the installation scripts.
