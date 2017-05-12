Developer Environment
=====================

Overview
--------
To facilitate app development, a semi-privileged **devuser** account is available on the Z9-PE-DEVKIT when the "Custom Apps" license has been applied.

The **devuser** account is accessed either via a serial terminal (when connected via a Micro-USB cable), or via SSH (when connected via the network). The specific application used doesn't matter. Tera Term (http://ttssh2.osdn.jp/index.html.en) is popular at FreeWave.

.. note:: This document provides basic information. Details are included in the ZumLink Z9-PE-DEVKIT User Manual.

Serial Connection
~~~~~~~~~~~~~~~~~
To use a serial terminal program, configure the serial port with these parameters:

=============   ===========
**Parameter**   **Setting**
=============   ===========
Baud Rate       115200
Data Bits       8
Parity          None
Stop Bits       1
Flow Control    None
=============   ===========

SSH Basics
~~~~~~~~~~
To use SSH, a network connection to the device is required. Either use a serial terminal program or the command line program.

**Example:**

.. raw:: html

    <pre class="cmdline">
    C:\dev> <b>devuser@192.168.111.100</b>
    devuser@192.168.111.100's password:
    freewave-ib:~$
    </pre>

.. note:: The factory default IP address of Z9-PE is 192.168.111.100. Examples shown in this documentation may differ from this default.

Developer File System
---------------------
The developer filesystem is a sandboxed chroot enviromnent distinct from the core system. It is open for read/write by the app developer. All applications, libraries, config files, etc. should be placed within this filesystem. The purpose of notable directories is listed below.

**/home/devuser**
    * The home directory of the **devuser** account.

**/home/apps**
    * The recommended location for installing custom user applications.

**/home/apps/template**
    * This is a template of what an app directory should look like.
    * Contains an example **run** script that can be used to launch the application if following the automatic service startup procedure described in :doc:`App Installation and Startup`.

**/ptp**
    * This is the directory that the user sees as the "ZumLink" PTP device when connected to a computer via a USB cable.

    * Files placed in here with extensions recognized by the device will be automatically be processed. These file extensions are:

    ==============  ================================
    **Extension**   **File Type**
    --------------  --------------------------------
    .pkg; .pkg.txt  Interface board firmware updates
    .cfg; .cfg.txt  Configuration changes
    .fcf; .fcf.txt  Radio module firmware updates
    ==============  ================================

.. _ptp-directory-contents:

PTP Directory Contents
~~~~~~~~~~~~~~~~~~~~~~
The purpose of the individual files is discussed in more detail in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_.


**/ptp/boot_results.txt**
    Shows the firmware version the device booted and is currently running.

**/ptp/config.txt**
    Shows the state of all configurable parameters of the device.

**/ptp/fw_upgrade_result.txt**
    Shows the status of a device firmware upgrade, if one has occurred.

**/ptp/help.txt**
    Describes CLI commands and configurable parameters of the device.

**/ptp/layout.txt**
    A YAML-formatted definition of configurable parameters for use by management applications.

**/ptp/modbuslayout.txt**
    Deprecated. Do not use.

**/ptp/result.txt**
    Contains the results of any configuration changes made by copying a .cfg or .cfg.txt file into the **ptp** directory.

**/ptp/sys_info.txt**
    Contains device identity properties.
