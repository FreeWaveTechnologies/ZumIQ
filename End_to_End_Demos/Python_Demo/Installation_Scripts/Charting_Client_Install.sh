!/bin/bash

echo '>>>>apt-get update'
sudo apt-get -y update

echo '>>>> setting date on device'
sudo apt-get install -y ntpdate
sudo ntpdate -u pool.ntp.org

echo '>>>>>apt-get vim python and pip'
sudo apt-get install -y vim python python-pip

echo '>>>>>installing paho-mqtt'
sudo pip install paho-mqtt

echo '>>>>>>installing Flask'
echo '>>>>>>COMMON ERROR -- if Flask installation fails, make sure the date on ZumLink IPR is correctly set to UTC date/time'
sudo pip install Flask

echo 'making templates directory'
mkdir -p /home/devuser/apps/Python_MQTT_Demo/templates

APPFILE=/home/devuser/apps/Python_MQTT_Demo/Charting_Client.py
JSFILE=/home/devuser/apps/Python_MQTT_Demo/templates/Charting_Client_Website.html

cat /home/devuser/apps/End_to_End_Sensor_MQTT_Demos/Python_MQTT_Demo/Charting_Client_Python_MQTT_Demo/Charting_Client.py > $APPFILE
cat /home/devuser/apps/End_to_End_Sensor_MQTT_Demos/Python_MQTT_Demo/Charting_Client_Python_MQTT_Demo/templates/Charting_Client_Website.html > $JSFILE

sudo chmod 777 /home/devuser/apps/Python_MQTT_Demo/Charting_Client.py
sudo chmod 777 /home/devuser/apps/Python_MQTT_Demo/templates/Charting_Client_Website.html
/home/devuser/apps/Python_MQTT_Demo/Charting_Client.py
