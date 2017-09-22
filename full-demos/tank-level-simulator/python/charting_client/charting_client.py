""" Tank Level Simulation Charting Client

This script demonstrates the following:
- Subscribe to sensor data via MQTT
- Display sensor data in a web page
"""

# ----------------------------------------------------------------------------
# BSD 2-Clause License
#
# Copyright (c) 2017, FreeWave Technologies
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import time

from flask import Flask, render_template
import paho.mqtt.client as mqtt

MOSQUITTO_ADDRESS = '127.0.0.1'
MOSQUITTO_PORT = 1883

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
    client.connect(MOSQUITTO_ADDRESS, MOSQUITTO_PORT, 60)
    client.loop_start()
    time.sleep(0.1)
    client.loop_stop()

@app.route('/')
def index():
    return render_template('charting_client_website.html')

''' /updater is an API endpoint to retrieve the latest
    data point for our JS handler '''
@app.route('/updater')
def updater():
    get_level()
    return str(level_collection[-1])

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
