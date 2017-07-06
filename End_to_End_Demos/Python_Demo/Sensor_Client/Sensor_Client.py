#!/usr/bin/python2.7

import minimalmodbus
import time
import paho.mqtt.client as mqtt
from Sensor_Client_Config import high_threshold, low_threshold

''' Serialbase variable is the modbus connection to the serial base device '''
serialbase = minimalmodbus.Instrument('/dev/ttyO1', 1)

''' After creating a client we connect to the ZumLink IPR itself, where the Mosquitto
broker is running, and publish sensor data to this broker on port 1890 on topic demo/sensors'''
mqttc = mqtt.Client("Sensor Levels")
mqttc.connect("127.0.0.1", 1890)
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

def change_LED(register, on_off):
    ''' Writing to the "channel mode" register of each LED turns the LED on or off. 4 is off, 5 is on'''
    serialbase.write_register(register, on_off)

while True:
    pot_level = read_pot_level()
    if pot_level >= high_threshold:
    	print_alert("over")
    	change_LED(40018,5)
	change_LED(40017,4)
    elif pot_level <= low_threshold:
    	print_alert("under")
    	change_LED(40017, 5)
	change_LED(40018, 4)
    else:
    	change_LED(40018, 4)
    	change_LED(40017, 4)
    	print_pot_level()
    time.sleep(.5)
