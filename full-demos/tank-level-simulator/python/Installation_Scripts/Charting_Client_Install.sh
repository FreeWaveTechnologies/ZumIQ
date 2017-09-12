#!/bin/bash

sudo apt-get update
sudo apt-get install -y vim python python-pip
sudo pip install -y paho-mqtt flask

cp -r ../Charting_Client ~/apps/Charting_Client

ln -s ~/sevices/Charting_Client ~/apps/Charting_Client

