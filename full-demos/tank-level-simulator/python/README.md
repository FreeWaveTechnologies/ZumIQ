# Python Tank Level Monitoring Simulator

## Source Code

The source code for each radio's application will be in the respective folders. "Sensor Client" is for the radio reading modbus registers and running Mosquitto, and  "Charting Client" is for the radio receiving and charting the sensor data. In this demo, both apps are run on the same radio for simplicity.

## Installation

The easiest way to get the apps running on a radio is to clone the Git repo and run the installation scripts included.

1. Login to the Z9-PE as "devuser" (See [Logging In](https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk/wiki/Logging-In) for details)

2. Clone the git repo with the demo code:

    git clone https://github.com/FreeWaveTechnologies/zumlink-ipr-sdk.git

3. Install Mosquitto using the built-in script

    install-mosquitto.sh

4. Run the demo script installers

    cd zumlink-ipr-sdk/full-demos/tank-level-simulator/python/installation-scripts
    ./sensor-client-install.sh
    ./charting-client-install.sh

5. Rotate the potentiometer between its limits. One LED should illuminate near one limit, and the other LED should illuminate at the other limit.

6. Open a browser to http://192.168.111.100:5000. You should see the potentiometer value update in real time.



    
