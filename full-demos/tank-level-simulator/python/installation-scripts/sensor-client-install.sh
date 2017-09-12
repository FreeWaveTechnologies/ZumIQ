#!/bin/bash

sudo apt-get update
sudo apt-get install -y python-pip
sudo pip install paho-mqtt minimalmodbus

cp -r ../sensor_client ~/apps/sensor_client

ln -s ~/apps/sensor_client ~/service/sensor_client
