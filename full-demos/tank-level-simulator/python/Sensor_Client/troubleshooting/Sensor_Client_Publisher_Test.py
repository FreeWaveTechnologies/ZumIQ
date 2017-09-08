import minimalmodbus
import time
import paho.mqtt.client as mqtt
from demo_config import high_threshold, low_threshold

serialbase = minimalmodbus.Instrument('/dev/ttyO1', 1)

mqttc = mqtt.Client("Sensor Levels")
mqttc.connect("127.0.0.1", 1890)
mqttc.publish("demo/sensors", "Hello this is sensors!")


def read_pot_level():
    return serialbase.read_float(30040, 4, 2)

def print_pot_level():
    print read_pot_level()
    mqttc.publish("demo/sensors", read_pot_level())

def change_LED(register, on_off):
    ''' Writing to the "channel mode" register of each LED turns the LED on or off. 4 is off, 5 is on'''
    serialbase.write_register(register, on_off)

while True:
    pot_level = read_pot_level()
    if pot_level >= high_threshold:
        print_pot_level()
	change_LED(40018,5)
        change_LED(40017,4)
    elif pot_level <= low_threshold:
	print_pot_level()
        change_LED(40017, 5)
        change_LED(40018, 4)
    else:
        change_LED(40018, 4)
        change_LED(40017, 4)
        print_pot_level()
    time.sleep(.5)
