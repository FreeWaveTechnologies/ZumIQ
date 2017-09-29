#!/bin/bash -x
sudo rm /etc/apt/sources.list.d/*node*.list
sudo apt-get remove -y nodejs
sudo apt-get update
sudo apt-get install -y locales ntpdate avahi-utils python build-essential curl
curl -sL https://deb.nodesource.com/setup_7.x > ~/bin/nodejs_setup
chmod 777 ~/bin/nodejs_setup
sudo ~/bin/nodejs_setup
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key > /tmp/nodesource.gpg.key
sudo apt-key add /tmp/nodesource.gpg.key
sudo apt-get install -y nodejs
rm ~/bin/nodejs_setup
