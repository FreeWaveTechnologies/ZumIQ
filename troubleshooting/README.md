# Troubleshooting

This folder contains scripts and procedures that can help work around known issues of the ZumIQ platform.

* [install-node7.sh](install-node7.sh) - This script will install Node.js v7. There is a bug in Node.js v8 that can cause web requests to timeout after only 1 second, which can cause issues on slow or high-latency networks. In particular, this can affect accessing the Node-RED website over some radio networks. This script will replace Node.js v8 as installed by the *install-node-red.sh* script in the */home/devuser/bin* folder. It can be run before or after installing Node-RED using the *install-node-red.sh" script. Note that this will make Node.js v7 the default for the entire ZumIQ Linux runtime.
 
