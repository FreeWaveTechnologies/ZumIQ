End to End Demos and Hardware Setup
===================================

These applications explore using a ZumLink to read Modbus data from a Serial Base, transmitting the data to a different radio, and charting it on the receiving radio.

Both Python and Node-RED follow the **same HardWare Setup which can be found below.**

For each demo there are three moving parts.

1) A client application picking up sensor data from a Serial Base

2) A Mosquitto broker dealing with MQTT messages

3) Another client application (on a different ZumLink IPR) subscribing to the MQTT sensor data from the broker, and charting the data live on a website.

Hardware Setup
==============

Road Map
--------
These are the goals of building the MQTT Demo App as well as a flow chart of how it works:

* To upload (or write) and run a small app in the ZumLink IPR Development Environment

* To interface ZumLink IPR with an IOE-4422 (Serial Base) with sensors connected to the Serial Base, and be able to read the sensors in the ZumLink IPR Development Environment

* To make this app in ZumLink IPR actuate devices (LEDS in this case) according to a sensor level that is read from the Serial Base

* To wirelessly transfer incoming voltage levels from one ZumLink IPR to another via the MQTT messaging protocol

* On the receiving ZumLink IPR, to create a live updating chart of the incoming voltage data

Hardware Tools
~~~~~~~~~~~~~~

=============================  =====================================================================================================================================
**Hardware**                   **Purpose**
-----------------------------  -------------------------------------------------------------------------------------------------------------------------------------
ZumLink IPR                    Radio with Linux Development Environment
IOE-4022                       Serial Base. This FreeWave Modbus device connects to sensors and sends data to ZumLink IPR
Ethernet to USB Cable          This will connect the ZumLink IPR's Ethernet port to a PC's USB port
RJ45 to DB9 Cable              This cable connects from an RJ45 Serial Port on ZumLink IPR to the Rainbow Cable, ensures communication between radio and Serial Base
Rainbow Cable (ASC3610DJ)      This cable connects from the DB9 end of the RJ45/DB9 cable to the Serial Base, ensures communication between radio and Serial Base
Potentiometer                  Will give off a voltage reading to simulate a sensor
Breadboard                     A board to make a circuit with a potentiometer and LEDs, and then connect it to the Serial Base
560Ω 0.5W resistors (2x)       To reduce the Serial Base voltage going to LEDs
Multimeter (optional)          For checking correct voltage levels from potentiometer and Serial Base
Jumper Wires                   Connect resistors, LEDs, etc on Breadboard
=============================  =====================================================================================================================================

**Note:** FreeWave's "Rainbow Cable" (ASC3610DJ Data Interface Cable) is a cable made specifically for FreeWave and should be ordered from the company.
**Note:** The terms IOE-4422, IOE, and Serial Base all refer to the same device and can be used interchangeably. For simplicity this document will usually refer to it as **"Serial Base"**

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/zumlink.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/serialBase.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/pot.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/bb.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/LEDS.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/rj.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/RainbowCable.JPG">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/ethernet.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/resistor.jpg">

.. raw:: html

   <img width=50 size=10 style="display:inline-block;" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/jumperWires.jpg">




.. image:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/zumlink.jpg
    :width: 150px

    **ZumLink IPR**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/serialBase.jpg
    :width: 150px

    **IOE-4422 Serial Base**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/pot.jpg
    :width: 150px

    **Potentiometer**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/bb.jpg
    :width: 150px

    **Breadboard**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/LEDS.jpg
    :width: 150px

    **LEDs**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/rj.jpg
    :width: 150px

    **Rj45 to DB9**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/RainbowCable.JPG
    :width: 150px

    **Rainbow Cable ASC3610DJ**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/ethernet.jpg
    :width: 150px

    **Ethernet to USB**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/resistor.jpg
    :width: 150px

    **560Ω Resistor**

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/jumperWires.jpg
    :width: 150px

    **Jumper Wires**

Software Tools
~~~~~~~~~~~~~~

=============================  ==========================================================================================================
**Software**                   **Purpose**
-----------------------------  ----------------------------------------------------------------------------------------------------------
FreeWave CLI                   Proprietary FreeWave Command Line Interface included in every ZumLink radio used to set radio's parameters
Tool Suite                     Downloadable FreeWave program used for reading and configuring Serial Bases and other products
Python 2.7                     Programming language used for writing software
Minimalmodbus                  Python library for easily reading and writing Modbus registers
Mosquitto                      Python library for creating MQTT brokers
paho-mqtt                      Python library for creating MQTT clients
jQuery                         JavaScript library, will be used here to help integrate the chart into a webpage
Highcharts                     JavaScript library for creating charts
=============================  ==========================================================================================================

Setting up the Serial Base and Breadboard
-----------------------------------------

Serial Base Channel I/O's
~~~~~~~~~~~~~~~~~~~~~~~~~

=============================  ============  ===========================================================================
**Channel**                    TS setting    **I/O**
-----------------------------  ------------  ---------------------------------------------------------------------------
Channel 1                      Sensor Power  Potentiometer
GND
Channel 2                      Sensor Power  Low Threshold LED (red)
GND
Channel 3                      Sensor Power  High Threshold LED (yellow)
GND
Channel 4
GND
Channel 5                      Analog In     Reading "sensor level" coming from potentiometer
GND
=============================  ============  ===========================================================================

Channel 1 sends power into the potentiometer.
Channel 2 sends power into the red LED.
Channel 3 sends power to the yellow LED.
Channel 5 reads the power level coming out of the potentiometer.

**Note:** (optional) Voltage level going into Channel 5 can be read on a computer using a Modbus program like Modbus Poll. The registers for it are 30040/30041 and should be set to **04 Read Input Registers**. The format for these registers should be **Float AB CD**

Serial Base Setup
~~~~~~~~~~~~~~~~~

Using Tool Suite, read the Serial Base that you are using with the button "Read Serial Base". Make sure to replicate these settings. In Tool Suite, the **channels** are to ensure communication with the **breadboard**, and the **Stack Settings** are to ensure communication between **ZumLink IPR and Serial Base**.

In Tool Suite, **Channels 1, 2, and 3** should all have the following settings:

====================  ===================
**Setting**           **Value**
--------------------  -------------------
I/O Mode              Sensor Power
Apply Default Output  Yes
Default Output        On
====================  ===================

**Channel 5** needs these settings:

==================  ===================
**Setting**         **Value**
------------------  -------------------
I/O Mode            Analog Input
Voltage or Current  Voltage
Zero Voltage        0
Voltage Span        12000
Resistor Pull       Pull-up
Filtering           None
Integer Type        Unsigned
==================  ===================

Then under **Stack Settings** for the Serial Base:

===============================  ===================
**Setting**                      **Value**
-------------------------------  -------------------
Serial Protocol                  RS-232
Port Speed                       19200
Parity                           None
Stop Bits                        1 bit
Modbus Address Mode              8 bit
Modbus ID:                       1 (match yours)
Modbus Message Interval          2
AI Integer Result Justification  Left
Floating Point word Order        Regular
Long Integer Word Order          Regular
Default Delay                    60
Power Mode                       Regular
===============================  ===================

**Note:** This demo will use COM port 2 on ZumLink IPR and give the Serial Base a Modbus ID of 1.

**Note:** To check that Serial Base is set up properly, test the sensor power outputs (Channel 1, 2, or 3) with a multimeter. Check to see that the output is close to 12 volts.

**Note:** A Port Speed (or BaudRate) of 19200 is fast enough, faster speeds could involve having to use Flow Control which is not covered in this document.

Potentiometer
~~~~~~~~~~~~~

With the turnable face of the potentiometer facing you:

* left most pin is **GND**
* middle pin is **Output Level**
* right most pin is **Power In**

LEDs
~~~~

The sensor power output of the Serial Base is 12 volts. This is **too much for an LED and can burn it out**, so we'll be using resistors to provide around 3 volts to the LEDs.

The basic flow will be power out from the channels of the Serial Base into the resistors, then from resistors to LED, then other LED pin to ground. The only exception is Channel 5 which will be an output from the middle pin of the potentiometer into Channel 5 set as Analog Input.

Putting the breadboard together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/schematic.png
    :width: 400px

    **Wiring Schematic**

Channel 1 is simply the power and GND to the potentiometer. Power goes into the rightmost pin, GND to the leftmost.

Channels 2 and 3 do the same thing, they each give power to an LED on the breadboard through the LED's anode. The LED's anodes need to be connected to GND.

Channel 5 needs a cable to connect with the middle pin of potentiometer (output voltage reading).

Using the Python library MinimalModbus we can:

1) Tell our app to read the level coming in from the potentiometer (Channel 5)

2) "Write" the registers for the channels 2 and 3 which send power to the LEDs. This way we control their state and are able to turn them on or off. We will do so depending on a conditional statement in our code saying: "If the low threshold is crossed turn on the red LED (set mode of channel 2 to Sensor Power), if the high threshold is crossed turn on the yellow LED (set mode of channel 3 to Sensor Power), if no thresholds are crossed then both LEDs should be off. (set mode of channels 2 and 3 to anything other than Sensor Power)"

To reduce the 12v from the Serial Base into a lower voltage that won't burn the LEDs we'll use 560Ω 0.5 Watt resistors.

ZumLink IPR Setup
-----------------

In order to connect the ZumLink IPR and Serial Base, two cables are needed. The Rainbow Cable that connects into the Serial Base, then a RJ45 to DB9 cable that connects the Rainbow Cable to COM port 2 on the ZumLink IPR.

In the FreeWave CLI, settings can be set to match the Serial Base to make sure communication is possible.

===============================  ===================
**Setting**                      **Value**
-------------------------------  -------------------
Com2.BaudRate                    19200
Com2.mode                        RS232
Com2.parity                      None
Com2.stopbits                    1
Com2.handler                     Setup
Com2.databits                    8
Com2.flowControl                 off
===============================  ===================

Internet into ZumLink IPR
~~~~~~~~~~~~~~~~~~~~~~~~~

Before we put any code into the ZumLink IPR, we need to **make sure the device is receiving internet**. Open a terminal on the ZumLink IPR and "ping 8.8.8.8". If it returns a stream of data, it's connected.

To do this:

1) Change 3rd Octet of ZIPR and Ethernet Adapter IP addresses to 137. Ex 192.168.137.100

**Note:** To change the radio IP address, enter the FreeWave CLI and enter command 'network.ip_address=***.***.137.***'. To change the ethernet adapter IP address, go to 'network settings', find the adapter that corresponds to the connected ZIPR, right click it, choose ipv4 properties, then change the IP address in there

2) Click on the adapter bringing internet into the computer (this can be WiFi or ethernet), then at the top of that menu there should be a tab 'Sharing'. Click it.

3) Click to enable sharing internet with connected devices. In the dropdown box select the corresponding connecting adapter for the ZIPR.

4) Make sure in FreeWave CLI that the setting "network.Gateway" has the correct IP address corresponding to the IP address of the network adapter where ZIPR is connected.

Troubleshooting Internet Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go into network adapters, click the internet source for your computer, then in 'sharing' tab, turn internet sharing off, click OK, then go back in and turn it back on. ZumLink IPR can remain connected to the computer while doing this.

Setting Up Communication between Two ZIPRs
------------------------------------------

Radio Settings
~~~~~~~~~~~~~~

The procedure for getting two ZIPRs to communicate entails making sure certain settings on both radios match, and then turning them on. The communication is automatic.

In each ZIPR, go to FreeWave CLI to set the following configuration values.

**Warning:** If both radios are within close distance to each other (a foot or less) the txPower needs to be turned down, otherwise hardware damage may occurr.

=============================  ====================================================================
**Setting Field**              **Value**
-----------------------------  --------------------------------------------------------------------
radioSettings.txPower          min (once radios are at a distance from each other, this can be raised)
radioSettings.radioFrequency   This number must be the same on both radios
radioSettings.networkId        This number must be the same on both radios
radioSettings.nodeId           Each radio must have unique number from 2-65533
=============================  ====================================================================
