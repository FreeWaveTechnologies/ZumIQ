Node-RED MQTT Demo Software Procedure
=====================================

Application Overview
--------------------

This application will have 3 moving parts on 2 ZumLink IPRs. The ZumLink IPR connected to the Serial Base and picking up sensor info will be referred to as the "Sensor Radio" and the other ZumLink IPR will be referred to as "Charting Radio" since it asks for that data and charts it. These are the 3 moving parts:

1) Client application on the Sensor Radio picking up sensor data from the Serial Base and sending it to the Mosquitto broker on Charting radio.

2) Mosquitto broker running on the Charting ZumLink IPR.

3) Client application on the Charting Radio which asks the Mosquitto broker for sensor information and then charts the data in the Node-RED interface.

Running Node-RED and Other Software
-----------------------------------

Before installing Node-RED it is wise to:

.. code-block:: none

  sudo apt-get update

  sudo apt-get upgrade

**Note:** Before installing Node-RED the date needs to be set and Node.js needs to be installed. To set the date use date command: "date 061920302017" where the first two digits are the month, second two digits are the day, next four digits are the time in UTC, and last four digits are the year (this example says June 19 20:30, 2017). Running the command "install-node.sh" from anywhere in the file system will set up Node.js and NPM.

To install Node-RED on each radio run the command:

.. code-block:: none

  install-node-red.sh

The file locations for installation are already configured and this command can be run from any location in the development environment.

 Mosquitto is needed on the Charting radio

.. code-block:: none

  sudo apt-get install mosquitto

After installing both Node-RED and mosquitto, they should be running automatically as a background process. To check type the command "ps -ef" and look for these processes.

If they are not running, reboot the device and then check. If at this point they are still not running by themselves on startup, they can be started with commands "node-red" and "mosquitto"

**Note:** Mosquitto will by default use port 1883 for communications and Node-RED will by default use port 1880 for its web GUI.

To see this active instance of Node-RED open a browser and go to the IP address of the radio just like with the web GUI, but go to port number 1880. This is the default Node-RED port.

Ex: 192.168.137.200:1880

Picking up the Sensor Information in Node-RED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sensor data will be picked up on the Sensor radio connected to the Serial Base.

In order to read ModBus in Node-RED an extra package needs to be downloaded, this package includes all nodes to handle Modbus. To download use this command "npm install -g node-red-contrib-modbus" and when that is done reboot the device. Node-RED will start itself on bootup and you should see the ModBus nodes.

With our instance of Node-RED open in the browser, drag a "Modbus Read" node into the workspace. Double click it to bring up its properties.

To connect to the Serial Base Modbus registers we set up these should be the specified settings in the "Modbus Read" node:

===============================  =========================
**Setting**                      **Value**
-------------------------------  -------------------------
FC                               FC 4 Read Input Registers
Address                          30040
Quantity                         2
Poll Rate                        1 second
Serial Port (under Server)       /dev/ttO1
Serial Type                      RTU
Baud Rate                        19200
===============================  =========================

At this point we will be reading floats from the Modbus registers, but these numbers need to be translated into a meaningful value- a voltage level. To do this translation drag a "function" node to the rights of the "Modbus Read" node, and connect the Output of "Modbus Read" node to the input of the new "function" node. Double click the "function" node to bring up its properties. Give it a name of "Converter" to avoid confusion with other "function" nodes later. Then in the space to put in code for the function put this in this code which turns the float into a voltage level:

.. code-block :: javascript

  var low = msg.payload[1];
  var high = msg.payload[0];
  var fpnum=low|(high<<16);
  var negative=(fpnum>>31)&1;
  var exponent=(fpnum>>23)&0xFF;
  var mantissa=(fpnum&0x7FFFFF);
  if(exponent==255){
    if(mantissa!==0)return Number.NaN;
    return (negative) ? Number.NEGATIVE_INFINITY : Number.POSITIVE_INFINITY;
  }
  if(exponent===0)exponent++;
  else mantissa|=0x800000;
  exponent-=127;
  var ret=(mantissa*1.0/0x800000)*Math.pow(2,exponent);
  if(negative)ret=-ret;
  return {payload:ret};

In order to see what is happening in Node-RED the "debug" node will send messages to the console called "debug" in Node-RED (similar to "console.log()" for you JavaScripters and "print" for Pythoneers). Drag one of these behind the output of the function. Then link "Converter"'s output to the debug node's input. This will by default console the msg.payload in the right side-bar under the "debug" tab. Clicking "deploy" is necessary for the program to start running, and upon doing that the voltage value set on the potentiometer should be displayed on that side bar as a continuous feed at the polling rate we set on the "Modbus Read" node.

Turning LED's on and off in Node-RED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two more steps in order to light up the LEDs when they cross a threshold. First we'll check the volatage level against a high and low threshold we will make, and second we'll turn the lEDs on/off.

.. note:: Node-RED will not allow any value other than "msg.payload" to be written to a Modbus register, or to make a chart with. It might be confusing as to why we're about to change msg.payload from a voltage level into an array with modbus register values, and then later turn msg.payload back into the voltage level. We **change msg.payload in order to write certain values to the registers** associated with giving power to the LED's, but after we will want msg.payload to **go back to voltage level so we can make a chart** with those incoming values. We'll store the initial msg.payload inside the variable msg.value to save it so it can be reverted back in the next step.

Let's drag another "function" node behind the "Converter" node and connect the output of "Converter" to the input of this "function" node, then let's name this node "Limit Checker". Here we want to check if msg.payload is more or less than a set threshold, we will use a low thresh of 2 and high of 10 as an example. Below is the code to go into the Limit Checker function node. What we return is an array with the values we want to write to the Modbus registers. If these array values are set to 5 or "Sensor Power" then 12v will be sent out and the LEDs will light up. If set to 4, there will be no voltage output and the LEDs will be off.

.. code-block:: javascript

  // When we change msg.payload we don't want to lose the voltage level that was read from the Modbus node, so we save that voltage level into msg.value, which we will use later.
  // We will create a msg.thresh message to inform of a low or high treshold being crossed.
  msg.value = msg.payload
  if(msg.payload < 2){
      msg.thresh = "Lo thresh crossed"
      msg.payload= [5,4]
  } else if(msg.payload > 10){
      msg.thresh = "Hi thresh crossed"
      msg.payload = [4,5]
  } else {
      msg.payload = [4,4]
  }
  return msg;

Now msg.payload contains the values we want to write to the Modbus registers corresponding to the serial base's output for giving voltage to the LED's, so we need to write these values to the registers. To do this drag a "Modbus Write" node behind the Limit Checker node, and connect the output of limit checker (the array that is now msg.payload) to the input of "Modbus Write". In the Modbus Write node the settings should be as follows:

===============================  ===============================
**Setting**                      **Value**
-------------------------------  -------------------------------
FC                               FC 16 Preset Multiple Registers
Quantity                         2
Address                          40017
Type                             Serial
Serial Port                      /dev/ttO1
Serial Type                      RTU
Baud Rate                        19200
===============================  ===============================

One last step is to set msg.payload **back to the voltage level**. Let's add a "function", name it "Reset Msg.Payload", connect its input as the output of LimitChecker (so Limit Checker will have two outputs) and the code for Reset Msg.Payload will be very simple since we saved the voltage level earlier as msg.value:

.. code-block:: javascript

  msg.payload = msg.value;
  return msg;

Setting Up Communication between Two ZumLink IPRs
-------------------------------------------------

Radio Settings
~~~~~~~~~~~~~~

The procedure for getting two ZumLink IPRs to communicate entails making sure certain settings on both radios match, and then turning them on. The communication is automatic.

In each ZumLink IPR, go to FreeWave CLI to set the following configuration values.

**Warning** If both radios are within close distance to each other (a foot or less) the txPower needs to be turned down

=============================  ====================================================================
**Setting Field**              **Value**
-----------------------------  --------------------------------------------------------------------
radioSettings.txPower          min (once radios are at a distance from each other, this can be raised)
radioSettings.radioFrequency   This number must be the same on both radios
radioSettings.networkId        This number must be the same on both radios
radioSettings.nodeId           Each radio must have unique number from 2-65533
=============================  ====================================================================

Setting up MQTT
---------------

At this point we will start talking about **two** Node-RED applications. The application that has been built so far is the **Sensor radio** application which picks up sensor information and sends it to the **Charting radio** radio, which receives the data and can chart the data stream in real time.

Starting the Client
~~~~~~~~~~~~~~~~~~~

Node-RED makes this quite simple. In the Node-RED web GUI for the client radio, the nodes on the left side-bar are categorized and under "output" there is a nod called "mqtt". Connecting the output of the Reset Msg.Payload node to the input of an "mqtt" node will make sure we are transmitting the msg.payload to the broker radio. In the settings for this output "mqtt" node we want to make the server address be the IP of the broker radio, and the port number the default 1883. For example: **192.168.137.100:1883**.

This will point the MQTT client to our Charting radio, and hook into Mosquitto's listening port. The topic can be whatever, it just has to match on the mqtt nodes of client and broker, the demo code uses "general" as the topic.

Starting the Broker
~~~~~~~~~~~~~~~~~~~

**Note:** There are several ways to do this since Node-RED does not come with a stock MQTT broker, only a subscriber. There is an extra node that can be downloaded which is an MQTT broker. In this example we will instead use the Mosquitto MQTT broker which already comes on ZumLink IPRs. Typing commanda "ps -ef" should reveal a running instance of a Mosquitto broker. This is activated on device bootup as a service.

If the command "ps -ef" does not show Mosquitto running, then start it with command "mosquitto". By default Mosquitto will use port 1883. This Mosquitto broker is running on the radio outside of Node-RED. The Charting radio's Node-RED instance will have an "mqtt" node that will subscribe to the Mosquitto broker, meaning this Charting radio has the Mosquitto broker as well as a subscriber "mqtt" node.

Since the client app is pointing at the Charting radio's IP address and Mosquitto port, communication should happen automatically. If it isn't make sure that node-RED on the Sensor radio and Mosquitto on the Charting radio are both running.


Charting MQTT Data Coming Into Broker ZumLink IPR
-------------------------------------------------

In order to make charts and display a dashboard on Node-RED it's necessary to download the "dashboard" nodes. On the Charting radio, this can be done simply by going to /home/devuser/apps and running command "npm i node-red-dashboard" then reboot the radio. Now the Node-RED web GUI will include a whole new set of nodes for making a dashboard view.

In the Charting radio's Node-RED web GUI, drag an "mqtt" node from the **input** section. This will subscribe to the Mosquitto broker and provide an output we can use to connect to a "chart" node. This "mqtt" node should have its "Server" property set as **127.0.0.1"** (pointing at its own IP address since its running the Mosquitto broker) and default port 1883.

Then drag a "chart" node into the workspace. In its settings we'll click the pencil symbol to add a new "Group", here the name can stay as "Default", but we need to click the pencil on the right hand side of "Tab" field. Inside the "Tab" options we can leave the Name as "Home" and "Icon" as "dashboard", just click the red Add button. Once back at the "Edit Chart Node" everything can stay the same except the "Y-axis" parameters where we want min to be 0 and max to be 12 for the range of voltages that will be fed into the chart.

The right hand side-bar now has a new tab named "dashboard". To see the dashboard, which will have the chart, click this tab, then on the top right hand corner there's a symbol of an arrow leaving a box. Clicking this symbol will open a new tab with the dashboard that holds the chart of incoming voltage levels being transmitted from the Sensor radio's Node-RED to the Charting radio's Mosquitto broker that then is subscribed to by the Charting radio's Node-RED and charted in the dashboard.
