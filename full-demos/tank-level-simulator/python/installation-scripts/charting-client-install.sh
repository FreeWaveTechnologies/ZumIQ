#!/bin/bash

sudo apt-get update
sudo apt-get install -y vim python python-pip
sudo pip install paho-mqtt flask

cp -r ../Charting_Client ~/apps/Charting_Client

ln -s ~/apps/Charting_Client ~/service/Charting_Client

