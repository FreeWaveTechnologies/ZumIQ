# Troubleshooting

This folder contains scripts and procedures that can help work around known issues of the ZumIQ platform.

* [install-node7.sh](install-node7.sh) - This script will install Node.js v7. There is an issue in Node.js v8 that can cause web requests to timeout on slow or high-latency networks. In particular, this can affect accessing the Node-RED website over some radio networks. This script will replace Node.js v8 as installed by the */home/devuser/bin/install-node-red.sh* script. It can be run before or after installing Node-RED using the *install-node-red.sh* script.

See the [**Known Issues**](https://github.com/FreeWaveTechnologies/ZumIQ/wiki/Known-Issues#node-red-website-timeout-on-slow-networks) page for more information.
