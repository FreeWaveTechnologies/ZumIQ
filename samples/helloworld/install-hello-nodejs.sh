#!/bin/bash

# This script creates and installs a simple "Hello World" app 
# using Node.js and the Express web framework.

echo ""
echo "WARNING: This is a basic script, and there is no error checking."
echo "If the script runs, but the hello world link doesn't work,"
echo "review the script output for any errors."
echo ""
read -p "Press <Enter> to continue"

# set up variables

HOMEDIR=/home/devuser
APPNAME=hello_nodejs
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.js
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/log.txt
MESSAGE='Hello, World, from Node.js!'
PORT=5400


# install prerequisites

curl -sL http://deb.nodesource.com/setup_6.x > /tmp/nodejs_setup
chmod 755 /tmp/nodejs_setup
sudo /tmp/nodejs_setup
sudo apt-get install -y nodejs
rm /tmp/nodejs_setup


# create the app

mkdir -p $APPDIR
cd $APPDIR

npm install express  # do this here to ensure that it's available to the app

echo "var express = require('express')" > $APPFILE
echo "var app = express()" >> $APPFILE
echo "" >> $APPFILE
echo "app.get('/hello', function(req, res) {" >> $APPFILE
echo "    res.send('$MESSAGE')" >> $APPFILE
echo "})" >> $APPFILE
echo "" >> $APPFILE
echo "app.listen($PORT, function() {" >> $APPFILE
echo "    console.log('Hello World app listening on port $PORT')" >> $APPFILE
echo "})" >> $APPFILE


# set up service

echo "#!/bin/sh" > run
echo "exec node $APPFILE > $LOGFILE 2>&1" >> run
chmod 755 run

ln -s $APPDIR $SERVICEDIR

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

