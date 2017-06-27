Source Code
===========

The source code for each radio's application will be in the respective folders. "Sensor Client" is for the radio reading modbus registers and "Charting Client" is for the radio receiving and charting the sensor data.

Installation Scripts
--------------------

Installation Scripts will contain a shell script for each client application. Running each script will take care of downloading all needed packages and providing the finished applications under /home/devuser/apps in the radios. If you are cloning this repo it is best to clone into /home/devuser.

Python MQTT Demo Software Procedure
===================================

**Note:** Instead of presenting all the code in this document, there will be a high level overview (pseudo-code) of what the code should be doing. All of the code is provided in a separate file.

The minimal modbus and publisher MQTT code is part of the Sensor Client, while the MQTT subscriber and website-chart will be part of the Charting Client.

Software Needed to get App Running
----------------------------------

**Warning:** The following procedure REQUIRES internet connection. If there are any issues with ZumLink IPR getting internet (check by pinging 8.8.8.8 on the device commandline) the way to fix this is by going to network adapters on the computer, disabling "internet sharing" on the adapter that is the internet source, and then re-enabling it.

First off:

.. code-block:: none

  sudo apt-get update

  sudo apt-get upgrade

then make sure Python and Pip are installed. If they aren't:

.. code-block:: none

  sudo apt-get install python-pip python-dev build-essential python2.7

To install Mosquitto:

.. code-block:: none

  sudo apt-get install mosquitto

**Note:** Mosquitto will start running automatically after installation. However it will not start automatically on device bootup.

We'll also need paho-mqtt, minimalmodbus, and Flask (which are Pip packages):

.. code-block:: none

  pip install paho-mqtt minimalmodbus Flask

Picking up the Sensor Information with Minimalmodbus on Sensor Client radio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Note:** MinimalModbus docs: http://minimalmodbus.readthedocs.io/en/master/index.html

For this project's Python code with comments: End_to_End_Sensor_MQTT_Demos/Python_MQTT_Demo/Sensor_Client_Python_MQTT_Demo/Sensor_Client.py

The process of using MinimalModbus in the code will be as follows:

1) Import minimalmodbus

2) Assign the Serial Base as the Modbus device that minimalmodbus will listen to by telling minimalmdobus which COM port to listen on.

.. code-block:: python

  serialbase = minimalmodbus.Instrument('/dev/ttyO1', 1)

**Warning:** Remember we are using COM2 for this example. If you are using COM1 the directory to listen is on **'/dev/ttyO5'**. The "O" in /dev/ttyO1 is the letter O, not a zero.

3) Now that minimalmodbus is included, and we have the variable 'serialbase' where it knows to listen for ModBus messages, we can read and write registers in this way:

.. code-block:: python

  serialbase.read_float(registerAddress, functionCode, number_of_registers_to_read)
  serialbase.write_register(registerAddress, value)

Setting up MQTT
---------------
MQTT needs two applications to be running, a broker and a client. We will use the Mosquitto library for a broker, and paho-mqtt for clients.

Mosquitto Broker
~~~~~~~~~~~~~~~~

**Note:** (optional) It's a good idea to setup MQTT communication only using one device at first. Using several terminal windows it's possible to start a broker and have a publisher and subscriber to test that this is working before attempting communicating between two radios.

It's a good idea to create a config file, to do this navigate to /etc/mosquitto/ and inside there create/edit a file "mosquitto.conf". It's possible you'll have to give yourself access to this file with "sudo chmod 777 mosquitto.conf". This is where mosquitto configuration will go. There's lots of config options, we will only use one line to specify which port Mosquitto will use:

.. code-block:: none

  port 1890

Then to start mosquitto type command

.. code-block:: none

  mosquitto -c mosquitto.conf

Another option to do this without a config file is to use flag -p (for port) and the number of the port. So the command would look like:

.. code-block:: none

  mosquitto -p 1890

Starting the paho-mqtt Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different types of clients for the MQTT protocol, a subscriber and a publisher. This document will cover the purpose and pseudo-code for each.

The subscriber simply finds the Mosquitto broker through the specified port and listens for messages that are published to the broker. Normally the subscriber will listen on certain "topics". These are the main built in functions this project will use for a subscriber client:

.. code-block:: python

  import paho.mqtt.client as mqtt
  client = mqtt.Client()
  # on_connect and on_message are the callback functions for MQTT events
  client.on_connect = on_connect
  client.on_message = on_message
  client.connect(<IP Adress>, <Port Number>, <Keep Alive Time>)

The publisher is the sender of messages to the broker. In this first example, the publisher will send the sensor information from the ZumLink IPR to a broker on the same radio. Then a subscriber on a separate radio will pick up that data by connecting to the broker. These are the main built in functions this project will use for a publisher client:

.. code-block:: python

  import paho.mqtt.client as mqttc
  client = mqtt.Client()
  client.connect(<IP Address of Broker>, <Port Number>)
  client.publish(<Topic>, <Message>)

Getting Mosquitto Communication Going
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have a broker program and a client app, we can put them together to talk.
In one terminal window start the broker with command "mosquitto -c mosquitto.conf"
A successful broker startup will give a message that looks like this:

.. code-block:: none

  freewave-ib:/etc/mosquitto$ mosquitto -c mosquitto.conf

  946688125: mosquitto version 1.3.4 (build date 2014-08-17 03:42:05+0000) startin

  946688125: Config loaded from /usr/sbin/mosquitto.conf

  946688125: Opening ipv4 listen socket on port 1890

  946688125: Opening ipv6 listen socket on port 1890

Then in a different terminal window start your client application. If the client and broker are communicating you should see connection messages for each. The broker's will look something like this:

.. code-block:: none

  946688322: New client connected from 127.0.0.1 as paho/F3E967D01F5D2A76AD (c1, k60).

Running Mosquitto across two ZumLink IPRs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make sure the radios are talking, open a terminal on one of the ZumLink IPRs and ping the other radio. If you receive information back, then communication is successful.

Now on the Sensro Client ZumLink IPR open a terminal and start a Mosquitto broker. "mosquitto -c mosquitto.conf"

In the Charting Client ZumLink IPR, open a terminal, and start the client program. This should look exactly like it did when we had a client and broker running on the same ZumLink IPR.

Building A Website to View Real Time Sensor Information
-------------------------------------------------------

For the final step we will implement a Flask/JavaScript web application in the Charting Client radio to be able to view our data real time.

The basics of this app will be:

1) Make a Flask application

2) Put minimalmodbus and MQTT code into the Flask app

3) Use Flask to render a website

4) In the HTML code for the website add the JavaScript

5) JavaScript will accept incoming sensor data from Flask and feed it into a chart

Example code is in Charting Client.
