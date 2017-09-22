# Web CLI Example

The "webcli_config.py" script demonstrates bare-bones acesss to the ZumLink Web CLI. Note that this is not a true RESTful API (state can be changed via HTTP GET methods), but is rather intended to be a simple shortcut to device configuration using an HTTP interface.

## Prerequisites

This sample uses the "requests" Python module. To install it, execute the following commands:
```bash
    sudo apt-get update
    sudo apt-get install python-pip
    sudo pip install requests
```
**NOTE:** "requests" is pulled in as a prerequsite of **pip**, so the final line above is included solely for explicitness.

## Usage

```bash
    python webcli_config.py
```

The progam will simply run thorugh a list of demonstrations and print the output to the console. It can be run either directly in the ZumIQ developer environment, or from a remote computer, as long as the IP address of the device is routable.