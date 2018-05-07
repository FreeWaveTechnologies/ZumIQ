# Getting Started with ZumIQ & Node-RED
## Example App #1 - Weather Station
##### Description: 
This app will request local weather data from an online source, display weather conditions in a dashboard, convert from Celsius to Fahrenheit and send e-mail notifications based upon weather data.
##### How to get started:
##### Setting up your Windows based computer :
The following section will grant ZumIQ access to your computer's Wi-Fi connection and configure the correct IP address for connection sharing.
1. Connect to a Wi-Fi network
2. Open Network and Sharing Center
3. Double-click the Wireless Network Connection in use
4. Click Properties then the Sharing tab
5. Click "Allow other network users to connect through this computer's internet connection"
6. Select "Local Area Connection" as the Home networking connection
7. Click OK then Close
##### Setting up ZumIQ on a FreeWave AppServer or ZumLink Radio

The following section will setup the ZumIQ environment to run the Weather Station App.

1. Connect to the ZumLink via a MircoUSB cable
2. Open the zumLink file storage _My Computer > ZumLink>(serial number)_
3. Save the following file to your desktop (link goes here)
4. Drag and drop file into the ZumLink file directory containing the system text files
5. Download & install the PuTTY terminal emulator 
[Download Here](https://the.earth.li/~sgtatham/putty/latest/w32/putty-0.70-installer.msi)
6. Launch PuTTY
7. Connect to _192.168.137.2_ on port 22 via SSH
8. Log in with _admin_ for both user and password
9. Type the following command and press enter: _rtereset hard_
10. Type the following command and press enter: _reset now_
-The hardware will take several minutes to reboot


##### Installing Node-RED on a FreeWave AppServer or ZumLink Radio
The following section will install Node-RED. Some commands may take several minutes to execute. The command is finished when the terminal returns to the devuser prompt.

1. Using PuTTY connect to _192.168.137.2_ on port 22 via SSH
2. Log in with _devuser_ for both user and password
3. Type the following command and press enter: _./bin/setdate.sh_
4. Type the following command and press enter: _cd bin && ./install-node-red.sh_
5. Type the following command and press enter: _./install-npm-modules.sh_
6. Type the following command and press enter: _cd ~/node-red/_
7. Type the following command and press enter: _npm install node-red-node-openweathermap_
8. Reboot ZumIQ with a power cycle. It may take several minutes to fully boot.

##### Accessing Node-RED on a FreeWave AppServer or ZumLink Radio

The following section will show you how to access the Node-RED interface and load the demonstration app.
1. Open a web browser and navigate to _192.168.137:1880_ or click [here](192.168.137.2:1880)
2. Click the button in the upper right hand corner > import > clipboard
3. Copy the contents of the *weather.json* file and paste into the  window.
4. Click Import then click Flow 1 at the top tabs
5. Deploy the app by click the Deploy button at the top
##### Creating an OpenWeather Account to Access Weather Data
You must create an account and generate an API key in order to access weather data.

1. Navigate to [here](https://home.openweathermap.org/users) and create an account – I ended up going to: https://home.openweathermap.org/users/sign_in 
2. After you gain access to the OpenWeather website click [here](https://home.openweathermap.org/api_keys)
3. Generate an API key. It will look something like _5609f402306022198e939a70178249d4_
4. Highlight your key then right click copy
5. Open the Node-RED interface and double click on the Weather Data Server node
6. Paste your API key into the API Key field then click Done and Deploy.

