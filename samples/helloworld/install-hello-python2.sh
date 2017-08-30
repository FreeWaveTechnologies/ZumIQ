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
using Python 2 and the Flask web framework.

WARNING: This is a basic script, and there is no error checking.
If the script runs, but the hello world link doesn't work, review
the script output for any errors.
"

read -p "Press <Enter> to continue"

# set up variables

HOMEDIR=/home/devuser
APPNAME=hello_python2
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.py
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/logs/current
MESSAGE='Hello, World, from Python 2!'
PORT=5200


# install prerequisites

sudo apt-get update
sudo apt-get install -y python python-pip
sudo pip2 install flask


# create the app

mkdir -p $APPDIR

echo "
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '$MESSAGE'""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=$PORT)
" > $APPFILE


# set up service

add-service.sh $APPNAME "python2 $APPFILE"

echo "Waiting 5 seconds to allow service to start up..."
sleep 5


# and we're done!

echo ""
echo "Python 2 Hello World app should be running"
echo "App is located at: $APPDIR"
echo "Service link is located at: $SERVICEDIR"
echo "Log file is located at: $LOGFILE"
echo ""
echo "Open a web browser and navigate to http://$(hostname -I | xargs):$PORT/hello"
echo "You should see the message: '$MESSAGE'"
