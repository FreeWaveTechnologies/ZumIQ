#!/bin/bash

sudo apt-get update
sudo apt-get install -y python-pip
sudo pip install paho-mqtt minimalmodbus

install-mosquitto.sh

cp -r ../Sensor_Client ~/apps/Sensor_Client

ln -s ~/apps/Sensor_Client ~/service/Sensor_Client
