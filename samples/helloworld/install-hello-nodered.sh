#!/bin/bash

# This script creates and installs a simple "Hello World" app 
# using the Node-RED platform.

echo ""
echo "WARNING: This is a basic script, and there is no error checking."
echo "If the script runs, but the hello world link doesn't work,"
echo "review the script output for any errors."
echo ""
read -p "Press <Enter> to continue"

# Set up variables

HOMEDIR=/home/devuser
APPNAME=hello_nodered
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.json
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/log.txt
NODEREDDIR=$HOMEDIR/.node-red
MESSAGE='Hello, World, from Node-RED!'
PORT=5500


# install prerequisites

# Node-RED runs on top of Node.js, so ensure that Node.js is installed first
curl -sL http://deb.nodesource.com/setup_6.x > /tmp/nodejs_setup
chmod 755 /tmp/nodejs_setup
sudo /tmp/nodejs_setup
sudo apt-get install -y nodejs
rm /tmp/nodejs_setup

# now install Node-RED
sudo apt-get install -y python build-essential
sudo npm install -g --unsafe-perm node-red


# create the app

mkdir -p $APPDIR
cd $APPDIR

echo '[{"id":"2d8507a0.b89e88","type":"tab","label":"Flow 1"},{"id":"1adad08a.c93cff","type":"http in","z":"2d8507a0.b89e88","name":"HTTP Request Handler","url":"/hello","method":"get","swaggerDoc":"","x":183,"y":118,"wires":[["e0f839bb.ae1fd8"]]},{"id":"e0f839bb.ae1fd8","type":"template","z":"2d8507a0.b89e88","name":"Hello Page","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"'$MESSAGE'","x":387,"y":118,"wires":[["e45b975f.b44a88"]]},{"id":"e45b975f.b44a88","type":"http response","z":"2d8507a0.b89e88","name":"HTTP Response Node","x":591,"y":118,"wires":[]}]' > $APPFILE


# set up service

echo "#!/bin/sh" > run
echo "exec node-red-pi --max-old-space-size=128 -u $NODEREDDIR -p $PORT $APPFILE > $LOGFILE 2>&1" >> run
chmod 755 run

ln -s $APPDIR $SERVICEDIR

echo "Waiting 20 seconds to allow service to start up..."
sleep 20

# and we're done!

echo ""
echo "Node-RED hello World app should be running"
echo "App is located at: $APPDIR"
echo "Service link is located at: $SERVICEDIR"
echo "Log file is located at: $LOGFILE"
echo ""
echo "Open a web browser and navigate to http://$(hostname -I | xargs):$PORT/hello"
echo "You should see the message: '$MESSAGE'"

