#!/usr/bin/python2.7

import minimalmodbus
import time
import paho.mqtt.client as mqtt
from Sensor_Client_Config import high_threshold, low_threshold

''' Serialbase variable is the modbus connection to the serial base device '''
serialbase = minimalmodbus.Instrument('/dev/ttyO1', 1)

''' After creating a client we connect to the ZumLink IPR itself, where the Mosquitto
broker is running, and publish sensor data to this broker on port 1883 on topic demo/sensors'''
mqttc = mqtt.Client("Sensor Levels")
mqttc.connect("127.0.0.1", 1883)
mqttc.publish("demo/sensors", "Hello this is sensors!")

def read_pot_level():
    return serialbase.read_float(30040, 4, 2)

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
        serialbase.write_bit(2,0)
        serialbase.write_bit(1,1)
    elif pot_level <= low_threshold:
    	print_alert("under")
        serialbase.write_bit(2,1)
        serialbase.write_bit(1,0)
    else:
        serialbase.write_bit(2,0)
        serialbase.write_bit(1,0)
    	print_pot_level()
    time.sleep(.5)
