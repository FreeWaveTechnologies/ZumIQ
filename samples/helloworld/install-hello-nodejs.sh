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
using Node.js and the Express web framework.

WARNING: This is a basic script, and there is no error checking.
If the script runs, but the hello world link doesn't work, review
the script output for any errors.
"
read -p "Press <Enter> to continue"

# set up variables

HOMEDIR=/home/devuser
APPNAME=hello_nodejs
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.js
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/logs/current
MESSAGE='Hello, World, from Node.js!'
PORT=5400


# install prerequisites

install-node.sh


# create the app

mkdir -p $APPDIR
cd $APPDIR

npm install express # install here to ensure proper pathing

echo "
var express = require('express')
var app = express()

app.get('/hello', function(req, res) {
    res.send('$MESSAGE')
})

app.listen($PORT, function() {
    console.log('Hello World app listening on port $PORT')
})
" > $APPFILE


# set up service

add-service.sh $APPNAME "node $APPFILE"

echo "Waiting 5 seconds to allow service to start up..."
sleep 5

# and we're done!

echo ""
echo "Node.js Hello World app should be running"
echo "App is located at: $APPDIR"
echo "Service link is located at: $SERVICEDIR"
echo "Log file is located at: $LOGFILE"
echo ""
echo "Open a web browser and navigate to http://$(hostname -I | xargs):$PORT/hello"
echo "You should see the message: '$MESSAGE'"

