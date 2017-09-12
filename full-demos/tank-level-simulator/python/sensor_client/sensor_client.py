""" Tank Level Simulation Sensor Client

This script demonstrates the following:
- Read value from a sensor (potentiometer) via Serial Base
- Publish sensor value via MQTT
- If sensor value exceeds thresholds, activate indicator LED via Serial Base    
"""

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

''' After creating a client we connect to the ZumLink IPR itself, where the Mosquitto
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
