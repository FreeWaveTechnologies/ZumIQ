#!/usr/bin/python2.7

import paho.mqtt.client as mqtt
from flask import Flask, render_template
import time

app = Flask(__name__)

level_received = ""
level_collection = []

def on_connect(client, userdata, rc, x):
    print("Connected with result code", str(rc))
    client.subscribe("demo/sensors")

def on_message(client, userdata, msg):
    global level_received
    print (msg.topic + " " + str(msg.payload))
    level_received = str(msg.payload)
    print "This is level received: ", level_received
    level_collection.append(level_received)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

''' connecting and disconnecting to get the latest
    data point '''
################ CHANGE IP ADDRESS BELOW ###############
def get_level():
    client.connect("192.168.137.200", 1890, 60)
    client.loop_start()
    time.sleep(0.1)
    client.loop_stop()

@app.route('/')
def index():
    return render_template('Charting_Client_Website.html')

''' /updater is an API endpoint to retrieve the latest
    data point for our JS handler '''
@app.route('/updater')
def updater():
    get_level()
    return str(level_collection[-1])

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
