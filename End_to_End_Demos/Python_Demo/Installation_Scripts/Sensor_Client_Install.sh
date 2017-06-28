!/bin/bash

echo '>>>> apt-get update <<<<'
sudo apt-get update

echo '>>>> setting date on device <<<<'
sudo apt-get install -y ntpdate
sudo ntpdate -u pool.ntp.org

echo '>>>> downloading vim, python, mosquitto <<<<'
sudo apt-get install -y vim python mosquitto

echo '>>>> downloading pip <<<<'
sudo apt-get install -y python-pip

echo '>>>> starting mosquitto on port 1890 <<<<'
echo mosquitto -p 1890 > mosquitto.sh
sudo chmod 777 mosquitto.sh
# cmd="mosquitto.sh"
# "${cmd}" &>/dev/null &disown

echo 'installing paho-mqtt, minimalmodbus'
sudo pip install paho-mqtt minimalmodbus

mkdir -p /home/devuser/apps/Sensor_Python_MQTT_Demo

APPFILE=/home/devuser/apps/Sensor_Client/Sensor_Client.py
DEMOCONFIG=/home/devuser/apps/Sensor_Client/Sensor_Client_Config.py
PYTHONDIR=${PWD%/*}

cat $PYTHONDIR/Sensor_Client/Sensor_Client.py > $APPFILE
cat $PYTHONDIR/Sensor_Client/Sensor_Client_Config.py > $DEMOCONFIG

echo 'starting mosquitto on port 1890, this will take over this CLI window'
echo 'open different window to start Sensor_Client.py'
mosquitto -p 1890
python /home/devuser/apps/Sensor_Python_MQTT_Demo/Sensor_Client.py
