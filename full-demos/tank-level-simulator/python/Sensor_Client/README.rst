End to End Demos and Hardware Setup
===================================
**Warning:** IP Addresses need to be changed in source code to match user's IP Addresses. The IP addresses in the demo are set to 192.168.137.100 for the Charting Client and 192.168.137.200 for the Sensor Client

These applications explore using a ZumLink IPR to read Modbus data from a Serial Base, transmitting the data to a different radio, and charting it on the receiving radio.

Both Python and Node-RED follow the **same Hardware Setup which can be found below.**

For each demo there are three moving parts:

1) A client application picking up sensor data from a Serial Base and pushing it to the MQTT broker.

2) An MQTT broker (Mosquitto) dealing with MQTT messages

3) Another client application (on a different ZumLink IPR) subscribing to the MQTT sensor data from the broker, and charting the data on a website.

Hardware Setup
==============

Road Map
--------
These are the goals of building the MQTT Demo App:

* To upload (or write) and run a small app in the ZumLink IPR Development Environment

* To interface ZumLink IPR with an IOE-4422 (Serial Base) with sensors connected to the Serial Base, and be able to read the sensors in the ZumLink IPR Development Environment

* To make this app in ZumLink IPR actuate devices (LEDs in this case) according to a sensor data that is read from the Serial Base

* To wirelessly transfer incoming sensor data from one ZumLink IPR to another via the MQTT messaging protocol

* On the receiving ZumLink IPR, to create a live updating website-chart of the incoming voltage data

Required Hardware
~~~~~~~~~~~~~~~~~

=============================  =====================================================================================================================================
**Hardware**                   **Purpose**
-----------------------------  -------------------------------------------------------------------------------------------------------------------------------------
ZumLink IPR                    Radio with Linux Development Environment
IOE-4022                       Serial Base. This FreeWave Modbus device connects to sensors and sends data to ZumLink IPR
Ethernet to USB Cable          This will connect the ZumLink IPR's Ethernet port to a PC's USB port
RJ45 to DB9 Cable              This cable connects from an RJ45 Serial Port on ZumLink IPR to the Rainbow Cable, ensures communication between radio and Serial Base
Rainbow Cable (ASC3610DJ)      This cable connects from the DB9 end of the RJ45/DB9 cable to the Serial Base, ensures communication between radio and Serial Base
Potentiometer                  Will give off a voltage reading to simulate a sensor
Breadboard                     Board that holds potentiometer, LED's, resistors, and jumper wires
560Ω 0.5W resistors (2x)       To reduce the Serial Base voltage going to LEDs
Multimeter (optional)          For checking correct voltage levels from potentiometer and Serial Base
Jumper Wires                   Connect resistors, LEDs, etc on Breadboard
=============================  =====================================================================================================================================

**Note:** FreeWave's "Rainbow Cable" (ASC3610DJ Data Interface Cable) is a cable made specifically for FreeWave and should be ordered from the company.

**Note:** The terms IOE-4422, IOE, and Serial Base all refer to the same device and can be used interchangeably. For simplicity this document will usually refer to it as **"Serial Base"**

.. raw:: html

   <p><img width=100% style="max-width:100%" src="https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/screenShot.png"></p>

Required Software
~~~~~~~~~~~~~~~~~

=============================  ==========================================================================================================
**Software**                   **Purpose**
-----------------------------  ----------------------------------------------------------------------------------------------------------
FreeWave CLI                   Proprietary FreeWave Command Line Interface included in every ZumLink radio used to set radio's parameters
Tool Suite                     FreeWave program used for reading and configuring Serial Base. `Download Here <http://www.freewave.com/tool-suite-programming-configuration-monitoring/>`_
Python 2.7                     Programming language
Minimalmodbus                  Python library for easily reading and writing Modbus registers
Mosquitto                      MQTT broker
paho-mqtt                      Python library for creating MQTT clients
Flask                          Python server framework to serve the website with a sensor data chart
jQuery                         JavaScript library, will be used here to help integrate sensor data chart into a webpage
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

Using Tool Suite, read the Serial Base that you are using with the button "Read Serial Base". Make sure to replicate these settings. In Tool Suite, the **Channels** are to ensure communication with the **breadboard**, and the **Stack Settings** are to ensure communication between **ZumLink IPR and Serial Base**.

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

**Note:** To check that a Serial Base is set up properly, test that setting channels in Tool Suite as "sensor power" gives outputs of around 12 volts.

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

.. figure:: https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/images/schematic.png
    :width: 400px

    **Wiring Schematic**

Channel 1 is simply the power and GND to the potentiometer. Power goes into the rightmost pin, GND to the leftmost.

Channels 2 and 3 each gives power to an LED on the breadboard. The LED's cathode needs to be connected to GND.

Channel 5 needs a cable to connect with the middle pin of potentiometer to read the output voltage.

Using the Python library MinimalModbus we can:

1) Tell our app to read the level coming in from the potentiometer (Channel 5)

2) "Write" the registers for the channels 2 and 3 which send power to the LEDs. This way we control their state and are able to turn them on or off. We will do so depending on a conditional statement in our code saying: "If the low threshold is crossed turn on the red LED (set mode of channel 2 to Sensor Power), if the high threshold is crossed turn on the yellow LED (set mode of channel 3 to Sensor Power), if no thresholds are crossed then both LEDs should be off. (set mode of channels 2 and 3 to anything other than Sensor Power)"

To reduce the 12v from the Serial Base into a lower voltage that won't burn the LEDs we'll use 560Ω 0.5 Watt resistors.

ZumLink IPR Setup
-----------------

In order to connect the ZumLink IPR and Serial Base, two cables are needed. The Rainbow Cable that connects into the Serial Base, then a RJ45 to DB9 cable that connects the Rainbow Cable to COM port 2 on the ZumLink IPR.

In the FreeWave CLI on the Zumlink IPR, settings can be set to match the Serial Base to make sure communication is possible.

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

Before we put any code into the ZumLink IPR, we need to **make sure the device is connected to the Internet**. Open a terminal on the ZumLink IPR, type "ping 8.8.8.8", and verify that the pings are successful. This is necessary to install software for package repositories.

Everyone's network is different. How you choose to configure your radios is largely up to you (and possibly your corporate IT department). The example below uses Internet Connection Sharing on Windows to give Internet access to a private network connected via a USB-to-Ethernet adapter.

To give internet access to a radio:

1) Change 3rd Octet of ZIPR and Ethernet Adapter IP addresses to 137. Ex 192.168.137.100 (remember to change this on the network adapter on the computer talking to your radio as well, otherwise the computer won't be able to communicate at all with the radio)

**Note:** To change the radio IP address, enter the FreeWave CLI and enter command 'network.ip_address=***.***.137.***'. To change the ethernet adapter IP address, go to 'network settings', find the adapter that corresponds to the connected ZumLink IPR, right click it, choose ipv4 properties, then change the IP address in there.

2) Double click on the adapter (in Network Settings) bringing internet into the computer (this can be WiFi or ethernet), then at the top of that menu there should be a tab 'Sharing'. Click it.

3) Click to enable sharing internet with connected devices. In the dropdown box select the corresponding connecting adapter for the ZumLink IPR.

4) Make sure in FreeWave CLI that the setting "network.Gateway" has the correct IP address corresponding to the IP address of the network adapter where ZIPR is connected.

Troubleshooting Internet Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ICS can sometimes be a bit touchy. Should you lose internet connectivity from the IPR, it may be necessary to reset the sharing on your PC. Go into network adapters, click the internet source for your computer, then in 'sharing' tab, turn internet sharing off, click OK, then go back in and turn it back on. ZumLink IPR can remain connected to the computer while doing this.

Setting Up Communication between Two ZumLink IPRs
-------------------------------------------------

Radio Settings
~~~~~~~~~~~~~~

The procedure for getting two ZumLink IPRs to communicate entails making sure certain settings on both radios match. Then communication will happen automatically. To test for communication, ping the IP address of one radio with the other. If you get a response, then they're talking. Also the CD and TX lights will flash green when communication is established.

In each ZumLink IPR, go to FreeWave CLI to set the following configuration values:

**Warning:** If both radios are within close distance to each other (a foot or less) the txPower needs to be turned down from the default 27dBm, otherwise **hardware damage may occurr**.

=============================  ====================================================================
**Setting Field**              **Value**
-----------------------------  --------------------------------------------------------------------
radioSettings.txPower          min (once radios are at a distance from each other, this can be raised)
radioSettings.radioFrequency   This number must be the same on both radios
radioSettings.networkId        This number must be the same on both radios
radioSettings.nodeId           Each radio must have unique number from 2-65533
=============================  ====================================================================
