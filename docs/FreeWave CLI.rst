FreeWave CLI
============

CLI Usage
---------
This section covers CLI use that is pertinent to common app development tasks. General CLI use is discussed in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_.

The CLI can be accessed using:

* the USB Serial connection
* any SSH client via either the Ethernet port, or
* a network connection over the radio network

When ZIPR functionality is licensed, in addition to the **admin** user, a new **devuser** account supporting app development will be enabled. The **admin** account is **less privileged** than the **devuser** account.

=============================  =============  ====================
**Account Type**               **User Name**  **Default Password**
-----------------------------  -------------  --------------------
Standard device administrator  admin          admin
App Developer                  devuser        devuser
=============================  =============  ====================

CLI examples
~~~~~~~~~~~~

.. note:: In these examples, use the IP address of your radio.

When logging in as **admin**, you will be taken directly to the ZumLink CLI:

.. raw:: html

    <pre class="cmdline">
    C:\> <b>ssh admin@192.168.111.100</b>
    admin@192.168.111.100's password:
    FreeWave Shell
    >
    </pre>

However, when logging is as **devuser**, you will be taken to the Linux Bash shell:

.. raw:: html

    <pre class="cmdline">
    C:\> <b>ssh devuser@192.168.111.100</b>
    devuser@192.168.111.100
    freewave-ib:~$ <b>pwd</b>
    /mnt/user_data/devuser
    freewave-ib:~$
    </pre>

From the Linux shell, there are two ways to access the ZumLink CLI.

1. Execute the **cliBridge** command with NO arguments. This will launch the interactive ZumLink CLI, from which behavior is identical had you logged in directly as **admin**:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:~$ <b>cliBridge</b>
    FreeWave Shell
    >
    </pre>

2. Execute the **cliBridge** command with a CLI argument. This will execute the CLI command, print the results to stdout, and return to the Bash shell:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:~$ <b>cliBridge pages</b>
    FreeWave Shell
    >pages
    Pages
        system
        systemInfo
        radioSettings
        radioSettingsHelpers
        encryption
        dataPath
        localDiagnostics
        config
        services
        network
        networkStats
        ntp
        Com1
        Com2
        date
        snmp
        security
        license

    RESULT:0:OK
    >exit
    freewave-ib:~$
    </pre>


.. note:: The FreeWave CLI is not case-sensitive (unlike the Linux Bash shell)

To return to the Linux Bash shell from the CLI, use the **exit** command:

.. raw:: html

    <pre class="cmdline">
    ><b>exit</b>
    freewave-ib:~$
    </pre>

CLI System Commands
-------------------
Once in the ZumLink CLI, there are a number of commands that can be issued and settings that can be configured. This section describes the commands and settings most pertinent to app development. Details on commands and settings can be found in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_.

Getting Help
~~~~~~~~~~~~

The **help** command (**system.help**) can be used to get additional information about:

* all commands and settings
* commands and settings on a specific page, or
* a specific command or setting.

**All Help Information**

For all commands and settings:

.. raw:: html

    <pre class="cmdline">
    ><b>help</b>
    <i>(results omitted for clarity)</i>
    </pre>

**Single Page Information**

To get help information for a single page, use the **help** command with the page name as an argument:

.. raw:: html

    <pre class="cmdline">
    ><b>help systemInfo</b>
    <i>(results omitted for clarity)</i>
    </pre>

**Single Command or Setting Help**

To get help information for a single command or setting, use the **help** command with the command or setting names as an argument:

.. raw:: html

    <pre class="cmdline">
    ><b>help radioSettings.txPower</b>
    =================================================================
                            radioSettings
    =================================================================
    radioSettings.txPower=5

        Transmit Power
        This item sets the transmit power. A higher power can be used
        to increase link margin. Use a lower transmit power to reduce
        interference when multiple radio links are in close proximity.
        The maximum transmit power can be limited if radioHoppingMode
        is set to Hopping_On. See frequencyMasks for more details.

        type:uint32_t min:0 max:30 default:27
            **Savable Configuration Item**
    -----------------------------------------------------------------
    RESULT:0:Ok
    </pre>

.. note:: If the setting or command name is unique across all pages,  you can eliminate the page name and just use the it directly (e.g., **help txPower**). This is true any time a command or parameter is accessed.

CLI Organization
~~~~~~~~~~~~~~~~
The CLI is organized into a series of pages, some containing commands, and others containing configurable parameters.

A list of all pages can be found by executing the **pages** command:

.. raw:: html

    <pre class="cmdline">
    ><b>pages</b>
    Pages
      system
      systemInfo
      radioSettings
      radioSettingsHelpers
      encryption
      dataPath
      localDiagnostics
      config
      services
      network
      networkStats
      ntp
      Com1
      Com2
      date
      snmp
      security
      license
    RESULT:0:OK
    >
    </pre>

=====================  ===============================================================
**Page**               **Description**
---------------------  ---------------------------------------------------------------
Com1                   Configuration of COM1 serial port
Com2                   Configuration of COM2 serial port
config                 Commands to manage configuration
dataPath               Configuration of how data is handled
date                   Contains assorted date and time parameters
encryption             Configuration of radio encryption parameters
license                Configuration of license settings
localDiagnostics       Read-only local diagnostics information
network                Configuration of Ethernet port and other network settings
networkStats           Read-only network statistics
ntp                    Configuration of Network Time Protocol settings
radioSettings          Configuration of the radio module
radioSettingsHelpers   Gives feedback on validity of radio settings
security               Configuration of miscellaneous security settings
services               Configuration of miscellaneous services
snmp                   Configuration of SNMP security settings
system                 System-level commands
systemInfo             Mostly read-only device description and identification settings
=====================  ===============================================================

Seeing All Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
To get the state of all configurable parameters (and see what commands are available), use the **dump** command:

.. raw:: html

    <pre class="cmdline">
    ><b>dump</b>
    [Page=system]
      help
      dump
      dumpPage
      dumpTag
      dumpFormat
      dumpFormat=Short
      showLayout

      (Results truncated for clarity)

    RESULT:0:OK
    >
    </pre>

Dump Format
~~~~~~~~~~~
system.dumpFormat changes the manner in which the results of CLI commands are returned. Despite the name, dumpFormat does NOT just affect the dump command, but rather affects the format of responses of ALL commands and setting changes.

**dumpFormat=Short**

Displays the page name in a header row, then each setting indented with its value, if applicable:

.. raw:: html

    <pre class='cmdline'>
    ><b>dumpFormat=Short</b>
    system.dumpFormat=Short
    RESULT:0:OK
    >
    ><b>network</b>
    [Page=network]
      mac_address=00:07:e7:00:00:68
      ip_address=192.168.1.101
      netmask=255.255.255.0
      gateway=192.168.1.1
      stpEnabled=false
      txqueuelen=25
      mtu=1500
      netmaskFilterEnabled=false
      nameserver_address1=8.8.8.8
      nameserver_address2=8.8.4.4
    RESULT:0:OK
    >
    </pre>

**dumpFormat=Full**

Displays each setting with its fully-qualified name and value(page.setting=value):

.. raw:: html

    <pre class='cmdline'>
    ><b>dumpFormat=Full</b>
    dumpFormat=Full
    RESULT:0:OK
    >
    ><b>network</b>
    network.mac_address=00:07:e7:00:00:68
    network.ip_address=192.168.1.101
    network.netmask=255.255.255.0
    network.gateway=192.168.1.1
    network.stpEnabled=false
    network.txqueuelen=25
    network.mtu=1500
    network.netmaskFilterEnabled=false
    network.nameserver_address1=8.8.8.8
    network.nameserver_address2=8.8.4.4
    RESULT:0:OK
    >
    </pre>

**dumpFormat=Verbose**

Same as "Full", but includes the page name in a header row, as with "Short":

.. raw:: html

    <pre class='cmdline'>
    ><b>dumpFormat=Verbose</b>
    dumpFormat=Verbose
    RESULT:0:OK
    >
    ><b>network</b>
    [Page=network]
    network.mac_address=00:07:e7:00:00:68
    network.ip_address=192.168.1.101
    network.netmask=255.255.255.0
    network.gateway=192.168.1.1
    network.stpEnabled=false
    network.txqueuelen=25
    network.mtu=1500
    network.netmaskFilterEnabled=false
    network.nameserver_address1=8.8.8.8
    network.nameserver_address2=8.8.4.4
    RESULT:0:OK
    >
    </pre>

**dumpFormat=Result**

Identical behavior to "Full".

**dumpFormat=Json**

Significantly different from other formats. Outputs result in JavaScript Object Notation:

.. raw:: html

    <pre class='cmdline'>
    ><b>dumpFormat=Json</b>

    Trying: dumpFormat=Json
    Old: system.dumpFormat=Result
    New: system.dumpFormat=Json
    ,"RESULT":{"RESULT":0, "MESSAGE":"OK"}}
    -------------BUG REPORTED CHANGE THIS LINE ABOVE ONCE FIXED-------

    >
    ><b>network</b>{"RESPONSE":
    {"pages":{
       "network":{
          "mac_address":"00:07:e7:00:00:68",
          "ip_address":"192.168.1.101",
          "netmask":"255.255.255.0",
          "gateway":"192.168.1.101",
          "stpEnabled":"false",
          "txqueuelen":"25",
          "mtu":"1500",
          "netmaskFilterEnabled":"false",
          "nameserver_address1":"8.8.8.8",
          "nameserver_address2":"8.8.4.4"}}}
    ,"RESULT":{"RESULT":0, "MESSAGE":"OK"}}
    >
    </pre>

.. note:: When using the web interface CLI, results are returned in JSON format, identical to the format when dumpFormat=Json.

Settings Layout
~~~~~~~~~~~~~~~
 Use the "showLayout" command to see a formal description of metadata for each setting.

.. raw:: html

    <pre class='cmdline'>
    ><b>showLayout</b>
    <i>(results omitted for clarity)</i>
    </pre>

This command returns a YAML representation of all pages and settings/commands. Content varies depending on the nature of the setting or command. the general form is:

.. raw:: html

    <pre class='cmdline'>
    <b>%YAML 1.1</b>
    ---

    pages:

       - page1:
          - setting1:
              (metadata fields)
          - setting2:
              (metadata fields)
       - page2:
          - setting3:
              (metadata fields)
          - setting4:
              (metadata fields)
       etc.
    </pre>

=================  ====================================================================================================================================================================================
**Metadata Type**  **Description**
-----------------  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
default            The default value of this setting
description        A detailed description of the setting
max                The maximum allowable value
min                The minimum allowable value
modbus             The Modbus register holding the value of the setting
options            A dictionary of discrete options for multiple-choice settings. When read, the name of the option will be returned, but the option can be set either by its name or its numeric value
size               The size of text field in characters
tags               A collection of tags indicating the scope of this setting
title              A short description of the setting
type               Internal data type representing this setting. Settings of type "execute" are commands that do some additional interal processing that may or may not return a value
=================  ====================================================================================================================================================================================


CLI Config Commands
-------------------
There are a number of configuration commands, however you will typically only ever need to concern yourself with the following three:

Rebooting the Radio
~~~~~~~~~~~~~~~~~~~
Execute the "config.reset=now" command:

.. raw:: html

    <pre class='cmdline'>
    ><b>reset=now</b>

    The system is going down for reboot NOW!(console) (Sat Jan 1 17:06:24 2000):
    freewave-ib:~$
    </pre>

.. note::  Unlike other CLI commands, there is no RESULT line that follows this command. The radio simply reboots.

Setting Factory Defaults
~~~~~~~~~~~~~~~~~~~~~~~~
Execute the "config.factoryDefaults=set" command:

.. warning:: Factory defaults are applied immediately. If you are connected to the radio via a network connection, that network connection will be lost, and you won't be able to contact the radio again. This command should only be executed when you have physical access to the radio and can configure it via Micro-USB port.

.. raw:: html

    <pre class='cmdline'>
    ><b>factoryDefaults=set</b>
    factoryDefaults=Defaults set
    RESULT:0:OK
    >freewave-ib:~$ Connection reset by 192.168.1.101
    C"\dev>
    </pre>

.. note:: Resetting factory defaults will only affect FreeWave CLI settings. It will not impact any files or apps in the Linux filesystem.

Persisting Configuration Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configuration changes are only saved temporarily and will not persist through a reboot unless explicitly saved. This gives the user the option to experiment with changes without committing them to flash storage.

Execute the "config.save=now" to persist change to flash, so that the changes will persist on a reboot.

.. raw:: html

    <pre class='cmdline'>
    ><b>save=now</b>
    config.save=Saved
    RESULT:0:OK
    >
    </pre>


CLI RuntimeEnvironment Commands
-------------------------------

Resetting the Developer Runtime Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The **rteReset** command can be used to reset the development environment.

===============  =========================================================================
**Command**      **Description**
---------------  -------------------------------------------------------------------------
rteReset=Hard    Completely deletes and resets the file system of the runtime environment. All user-generated content and settings are deleted (*/ptp* excluded). Reset takes place when device is rebooted.
rteReset=Soft    Refreshes the file system of the runtime environment by overwriting just the files that are part of the default runtime environment. User-generated content is not affected (unless default files were edited). Reset takes place when the device is rebooted.
rteReset=Cancel  Cancels the reset operation (clears the "Hard" or "Soft" reset flag) and prevents a reset on reboot.
===============  =========================================================================

.. raw:: html

    <pre class='cmdline'>
    ><b>rteReset=Hard</b>
    rteReset=Runtime environment hard reset scheduled for next boot.
    RESULT:0:OK
    ><b>rteReset=Soft</b>
    rteReset=Runtime environment soft reset scheduled for next boot.
    RESULT:0:OK
    ><b>rteReset=Cancel</b>
    rteReset=Runtime environment reset cancelled.
    RESULT:0:OK
    >
    </pre>

.. note:: The reset operation does not affect the */ptp* directory (which has special meaning to the system), so */ptp* can be used as a temporary backup location during a reset operation. FreeWave recommends that a single **tar** file be created for storage in the */ptp* directory, so as not impact the operation of the core system.

Key CLI Settings
----------------
For a comprehensive list of all Z9-PE settings and commands, refer to the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_. Settings most relevant for app development are listed below.

.. note:: The setting descriptions below indicate their default values.

SystemInfo Page
~~~~~~~~~~~~~~~

====================  =========================================
**Setting**           **Description**
--------------------  -----------------------------------------
serialNumber          The device serial number (read-only)
radioFirmwareVersion  The radio module firmware version (read-only)
deviceName            The user-supplied device name (writable)
deviceId              The Modbus ID of the device (writable)
license               Lists any license applied to this unit. "Custom Apps" indicates that the unit is licensed for app development. (read-only)
====================  =========================================

.. note:: Only **deviceName** and **deviceId** settings are user-writable on the SystemInfo pages. All other settings are read-only.

COM1 and COM2 Pages
~~~~~~~~~~~~~~~~~~~

**handler**

Most serial port settings should be familiar. The **handler** setting requires additional explanation.

======================  ========================================================
**Setting**             **Description**
----------------------  --------------------------------------------------------
handler=TerminalServer  The default setting. Serial data is passed through to the Ethernet port on the TCP port assigned to the TerminalServerPort setting.
handler=Cli             The FreeWave CLI will be exposed on the serial port
handler=Trace           The FreeWave CLI will be exposed on the serial port with trace enabled (for FreeWave internal use only).
handler=Setup           The serial port will be setup and then released to the operating system for control. When set for COM1, COM1 will be accessible as */dev/ttyO5*. When set for COM2, COM2 will be accessible as */dev/ttyO1*
======================  ========================================================

Network Page
~~~~~~~~~~~~

===========================  ===============================
**Setting**                  **Description**
---------------------------  -------------------------------
ip_address=192.168.111.100   IP address of the unit
netmask=255.255.255.0        Subnet mask of the unit
gateway=192.168.111.1        Network gateway of the unit
nameserver_address1=8.8.8.8  Primary DNS server IP address
nameserver_address2=8.8.4.4  Secondary DNS server IP address
===========================  ===============================

Security Page
~~~~~~~~~~~~~

========================  ============================================================================
**Setting**               **Description**
------------------------  ----------------------------------------------------------------------------
enablePtpInterface=true   Controls whether the PTP interface is available

                          true - PTP interface is enabled

                          false - PTP interface is disabled

                          .. note:: When disabled, the ZumLink device will not be present in Windows File Explorer, and drag-and-drop configuration will not be available
enableEthernetLogin=true  Controls whether logins are possible via the Ethernet port

                          true - Ethernet logins are enabled

                          false - Ethernet logins are disabled

                          .. note:: When disabled, you will not be able to SSH into the radio remotely
========================  ============================================================================

Services Page
~~~~~~~~~~~~~

==============  ============================================
**Setting**     **Description**
--------------  --------------------------------------------
timeOutCli=900  This command defines the amount of time (in seconds) that the CLI will stay active without any user input. After this timeout expires, the user will be dropped back to the Bash shell (if logged in as "devuser"), or the connection to the device will be closed (if logged in as "admin")
==============  ============================================
