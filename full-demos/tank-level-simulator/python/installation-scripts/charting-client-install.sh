#!/bin/bash

sudo apt-get update
sudo apt-get install -y vim python python-pip
sudo pip install paho-mqtt flask

cp -r ../charting_client ~/apps/charting_client

ln -s ~/apps/charting_client ~/service/charting_client

