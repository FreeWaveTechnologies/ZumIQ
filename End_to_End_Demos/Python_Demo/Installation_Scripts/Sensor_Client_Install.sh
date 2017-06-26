!/bin/bash

echo 'apt-get -y update'
sudo apt-get update

echo 'apt-get -y upgrade'
sudo apt-get upgrade

echo 'apt-get vim'
sudo apt-get install -y vim

echo 'apt-get python'
sudo apt-get install -y python

echo 'apt-get install mosquitto'
sudo apt-get install -y mosquitto

echo 'starting mosquitto on port 1890'
echo mosquitto -p 1890 > mosquitto.sh
sudo chmod 777 mosquitto.sh
cmd="mosquitto.sh"
"${cmd}" &>/dev/null &disown

echo 'apt-get python-pip'
sudo apt-get install -y python-pip

echo 'installing paho-mqtt and minimalmodbus'
sudo pip install paho-mqtt minimalmodbus

mkdir -p /home/devuser/apps/Sensor_Python_MQTT_Demo

APPFILE=/home/devuser/apps/Sensor_Python_MQTT_Demo/Sensor_Client.py
DEMOCONFIG=/home/devuser/apps/Sensor_Python_MQTT_Demo/Sensor_Client_Config.py

cat /home/devuser/apps/End_to_End_Sensor_MQTT_Demos/Python_MQTT_Demo/Sensor_Client_Python_MQTT_Demo/Sensor_Client.py > $APPFILE
cat /home/devuser/apps/End_to_End_Sensor_MQTT_Demos/Python_MQTT_Demo/Sensor_Client_Python_MQTT_Demo/Sensor_Client_Config.py > $DEMOCONFIG

echo 'starting mosquitto on port 1890, this will take over this CLI window.'
mosquitto -p 1890
python /home/devuser/apps/Sensor_Python_MQTT_Demo/Sensor_Client.py
