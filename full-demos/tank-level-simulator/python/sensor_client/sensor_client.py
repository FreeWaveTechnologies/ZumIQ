""" Tank Level Simulation Sensor Client

This script demonstrates the following:
- Read value from a sensor (potentiometer) via Serial Base
- Publish sensor value via MQTT
- If sensor value exceeds thresholds, activate indicator LED via Serial Base    
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

import minimalmodbus
import paho.mqtt.client as mqtt

from sensor_client_config import high_threshold, low_threshold

MOSQUITTO_ADDRESS = '127.0.0.1'
MOSQUITTO_PORT = 1883

# Channel 2 & 3 sensor power toggle coils
CH2_COIL = 1
CH3_COIL = 2

# Channel 5 analog input
CH5_INPUT_REGISTER = 30040
CH5_FUNCTION_CODE = 4
CH5_REGISTER_COUNT = 2

# Set up connection to Serial Base (via COM2)
serialbase = minimalmodbus.Instrument('/dev/ttyO1', 1)

''' After creating a client we connect to the Z9-PE itself, where the Mosquitto
broker is running, and publish sensor data to this broker on port 1883 on topic demo/sensors'''
# Set up connection to MQTT broker
mqttc = mqtt.Client("Sensor Levels")
mqttc.connect(MOSQUITTO_ADDRESS, MOSQUITTO_PORT)
mqttc.publish("demo/sensors", "Hello this is sensors!")

def read_pot_level():
    return serialbase.read_float(CH5_INPUT_REGISTER, CH5_FUNCTION_CODE, CH5_REGISTER_COUNT)

def print_pot_level():
    print read_pot_level()
    mqttc.publish("demo/sensors", read_pot_level())

def print_alert(over_under):
    over_under = over_under.upper()
    print "Alert! Current level of " + str(read_pot_level()) + " " + over_under + " threshold. "
    print "High threshold: " + str(high_threshold) + ". Low threshold: " + str(low_threshold)
    mqttc.publish("demo/sensors", pot_level)

while True:
    pot_level = read_pot_level()
    if pot_level >= high_threshold:
    	print_alert("over")
        serialbase.write_bit(CH3_COIL, 0)
        serialbase.write_bit(CH2_COIL, 1)
    elif pot_level <= low_threshold:
    	print_alert("under")
        serialbase.write_bit(CH3_COIL, 1)
        serialbase.write_bit(CH2_COIL, 0)
    else:
        serialbase.write_bit(CH3_COIL, 0)
        serialbase.write_bit(CH2_COIL, 0)
    	print_pot_level()
    time.sleep(0.5)
