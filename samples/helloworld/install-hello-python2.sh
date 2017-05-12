#!/bin/sh

# This script creates and installs a simple "Hello World" app
# using Python 2 and the Flask web framework.

# set up variables

HOMEDIR=/home/devuser
APPNAME=hello_python2
APPDIR=$HOMEDIR/apps/$APPNAME
APPFILE=$APPDIR/hello.py
SERVICEDIR=$HOMEDIR/service/$APPNAME
LOGFILE=$APPDIR/log.txt
MESSAGE='Hello, World, from Python2!'
PORT=5200


# install prerequisites

sudo apt-get install -y python python-pip
sudo pip2 install flask


# create the app

mkdir -p $APPDIR
cd $APPDIR

echo "from flask import Flask" > $APPFILE
echo "app = Flask(__name__)" >> $APPFILE
echo "" >> $APPFILE
echo "@app.route('/hello')" >> $APPFILE
echo "def hello():" >> $APPFILE
echo "    return '$MESSAGE'" >> $APPFILE
echo "" >> $APPFILE
echo "if __name__ == '__main__':" >> $APPFILE
echo "    app.run(host='0.0.0.0', port=$PORT)" >> $APPFILE


# set up service

echo "#!/bin/sh" > run
echo "exec python2 $APPFILE > $LOGFILE 2>&1" >> run
chmod 755 run

ln -s $APPDIR $SERVICEDIR


# and we're done!

echo ""
echo "Python 2 Hello World app should be running"
echo "App is located at: $APPDIR"
echo "Service link is located at: $SERVICEDIR"
echo "Log file is located at: $LOGFILE"
echo ""
echo "Open a web browser and navigate to http://$(hostname -I | xargs):$PORT/hello"
echo "You should see the message: '$MESSAGE'"

