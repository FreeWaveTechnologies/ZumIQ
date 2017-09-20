# Software and Radio Setup

## Configure Network

In order to pull packages and install dependencies, a connection to the Internet is required. Satisfying this requirement typically has two components:

1. Set up path to the Internet from the network the radio is connected to.
2. Configure settings on the ZumLink radio

### Set up path to internet

Setting up a path to the Internet depends on your network infrastructure and IT department. For example, you may be able to attach your radios to the corporate intranet, or use NAT to link private radio network attached to your computer to your corporate intranet.

### Configure network settings on radio

On the radio, you will need to configure the network settings on the Network pages of the CLI to match your external network configuration. These examples will used the default radio settings. (See the [ZumIQ Wiki](https://github.com/FreeWaveTechnologies/ZumIQ/wiki) or the [Z9-P/PE User Manual](http://support.freewave.com/knowledge-base/z9-pe-user-manual/) for details on how to configure the device):

    network.ip_address=192.168.111.100
    network.netmask=255.255.255.0
    network.gateway=192.168.111.1
    nameserver_address1=8.8.8.8
    nameserver_address2=8.8.4.4
    
To test connectivity to the internet, type `ping 8.8.8.8` at the Linux command line. If you get a positive response, you're connected.

## Configure Serial Port

Configure COM2 on a ZumLink radio to have the following settings. (See the [ZumIQ Wiki](https://github.com/FreeWaveTechnologies/ZumIQ/wiki) or the [Z9-P/PE User Manual](http://support.freewave.com/knowledge-base/z9-pe-user-manual/) for details on how to configure the device):

**Setting**      | **Value**
---------------- | -------------------
Com2.handler     | Setup
Com2.BaudRate    | 19200
Com2.mode        | RS232
Com2.parity      | None
Com2.stopbits    | 1
Com2.databits    | 8
Com2.flowControl | off

**NOTE:** After changing configuration, be sure to execute **save now** to persist settings and **reset now** to reboot and apply the changes to the COM port.

## Configure Mosquitto

Mosquitto is included by default with ZumIQ. To set it up as a service, run the included install script:

    install-mosquitto.sh

This will start the Mosquitto service immediately and ensure that it is running after a reboot.

## Next Steps

See [Python App](python/README.md) or [Node-RED App](node-red/README.md) for instructions on creating the Sensor and Charting client apps.
