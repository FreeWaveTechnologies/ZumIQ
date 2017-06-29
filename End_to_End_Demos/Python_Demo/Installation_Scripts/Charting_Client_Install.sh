!/bin/bash

echo '>>>>apt-get update <<<<'
sudo apt-get -y update

echo '>>>> setting date on device <<<<'
sudo apt-get install -y ntpdate
sudo ntpdate -u pool.ntp.org

echo '>>>>>apt-get vim python and pip <<<<'
sudo apt-get install -y vim python python-pip

echo '>>>>>installing paho-mqtt <<<<'
sudo pip install paho-mqtt

echo '>>>> installing Flask <<<<'
sudo pip install Flask

echo '>>>> making templates directory <<<<'
mkdir -p /home/devuser/apps/Charting_Client/templates

APPFILE=/home/devuser/apps/Charting_Client/Charting_Client.py
JSFILE=/home/devuser/apps/Charting_Client/templates/Charting_Client_Website.html
PYTHONDIR=${PWD%/*}

cat $PYTHONDIR/Charting_Client/Charting_Client.py > $APPFILE
cat $PYTHONDIR/Charting_Client/templates/Charting_Client_Website.html > $JSFILE

sudo chmod 777 /home/devuser/apps/Python_MQTT_Demo/Charting_Client.py
sudo chmod 777 /home/devuser/apps/Python_MQTT_Demo/templates/Charting_Client_Website.html
/home/devuser/apps/Python_MQTT_Demo/Charting_Client.py
