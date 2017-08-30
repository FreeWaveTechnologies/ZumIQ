#!/bin/bash

# ----------------------------------------------------------------------------
# BSD 2-Clause License
#
# Copyright (c) 2017, FreeWave Technologies
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

echo "
This script creates and installs a simple \"Hello World\" app
using Node-RED platform.

WARNING: This is a basic script, and there is no error checking.
If the script runs, but the hello world link doesn't work, review
the script output for any errors.
"
read -p "Press <Enter> to continue"

# Set up variables

HOMEDIR=/home/devuser
APPNAME=hello_nodered
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.json
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/log.txt
NODEREDDIR=$HOMEDIR/node-red
MESSAGE='Hello, World, from Node-RED!'
PORT=5500


# install prerequisites

install-node-red.sh


# create the app

mkdir -p $APPDIR

echo '
[{"id":"2d8507a0.b89e88","type":"tab","label":"Flow 1"},{"id":"1adad08a.c93cff","type":"http in","z":"2d8507a0.b89e88","name":"HTTP Request Handler","url":"/hello","method":"get","swaggerDoc":"","x":183,"y":118,"wires":[["e0f839bb.ae1fd8"]]},{"id":"e0f839bb.ae1fd8","type":"template","z":"2d8507a0.b89e88","name":"Hello Page","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"'$MESSAGE'","x":387,"y":118,"wires":[["e45b975f.b44a88"]]},{"id":"e45b975f.b44a88","type":"http response","z":"2d8507a0.b89e88","name":"HTTP Response Node","x":591,"y":118,"wires":[]}]
' > $APPFILE


# set up service

add-service.sh $APPNAME "node-red-pi --max-old-space-size=128 -u $NODEREDDIR -p $PORT $APPFILE"


echo "Waiting 25 seconds to allow service to start up..."
sleep 25

# and we're done!

echo ""
echo "Node-RED hello World app should be running"
echo "App is located at: $APPDIR"
echo "Service link is located at: $SERVICEDIR"
echo "Log file is located at: $LOGFILE"
echo ""
echo "Open a web browser and navigate to http://$(hostname -I | xargs):$PORT/hello"
echo "You should see the message: '$MESSAGE'"

