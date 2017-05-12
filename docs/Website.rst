Website
=======
The Z9-PE website provides a means to quickly view or change settings and upload files and firmware updates. It operates in two modes. By default, device settings cannot be changed directly. In configuration mode, however, device settings can be changed. :ref:`website-config-mode` is discussed below.

Additional information can be found in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_.

.. _website-default-mode:

Default Mode
------------
In a browser, navigate to ``http://<device-ip-address>``. The home page shows system information:

.. figure:: images/ZLwebpic1.png
    :width: 550px

    **Default Home Page**

The menu items are:

* :ref:`website-user-data`
* :ref:`website-file-upload`
* :ref:`website-system-info`
* :ref:`website-config` (Visible in :ref:`website-config-mode` only)
* :ref:`website-help`
* :ref:`website-logout`

.. _website-user-data:

User Data - Drag and Drop Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This page shows the contents of the */ptp* directory.

.. note:: This is the same directory available in File Explorer when connected via a USB cable.

.. figure:: images/ZLwebpic2.png
    :width: 550px

    **User Data Page**

.. _website-file-upload:

File Upload
~~~~~~~~~~~
This page allows a user to upload a file to the */ptp* directory.

.. note:: Files with specific recognized extensions will be processed automatically and do not appear in the directory. This includes configuration and firmware files, which are automatically applied (and may reboot the radio).

================  ================================
**Extension**     **File Type**
----------------  --------------------------------
*.pkg; .pkg.txt*  Interface board Firmware updates
*.cfg; .cfg.txt*  Configuration changes
*.fcf; .fcf.txt*  Radio module firmware updates
================  ================================

.. figure:: images/ZLwebpic3.png
    :width: 550px

    **File Upload Page**

.. _website-system-info:

System Info
~~~~~~~~~~~
This page allows the user to explore settings organized by the device page. The pages are the same as in the CLI. This is simply a visual representation of each setting.

.. note:: The values on the System Info page are read-only. To change settings, you must use one of the following methods:

* Drag-and-Drop a config file onto the device folder in File Explorer
* Use the FreeWave CLI via a serial terminal through the USB port
* Use the FreeWave CLI via an SSH connectin over the network
* Use :ref:`website-config-mode`
* Use the :ref:`website-web-cli`

.. figure:: images/ZLwebpic4.png
    :width: 550px

    **System Info Page**

.. _website-help:

Help
~~~~
Displays the help file. The content is the same as executing the "help" command from the CLI.

.. figure:: images/ZLwebpic5.png
    :width: 550px

    **Help Page**

.. _website-logout:

Logout
~~~~~~
Logs out of the device.

.. figure:: images/ZLwebpic6.png
    :width: 400px

    **Logout Popup**

.. _website-config-mode:

Configuration Mode
------------------

Whenever the device boots the website comes up in default mode, with all of the functionality described in :ref:`website-default-mode`. Config mode adds an additional Configuration menu item, allowing direct configuration of device settings via the device website.

To enable config mode, in a browser, navigate to ``http://<device-ip-address>/config``.

.. figure:: images/ZLweb-config-mode.png
    :width: 550px

    **Configuration Mode Home Page**

.. note:: Configuration mode, once enabled, remains enabled until the device is rebooted. You can use the default address of ``http://<device-ip-address>`` to access the configuration functionality.

.. _website-config:

Configuration
~~~~~~~~~~~~~

Configuration pages are very similar in appearance to the :ref:`website-system-info` pages. Unlike the read-only System Info pages, the Configuration pages allow modification of device settings.

Each page contains settings of three different types:
    * free text entry boxes
    * drop-down multiple-choice lists
    * read-only parameters (such as diagnostic or identity parameters)

The settings are identical to those available in the CLI, and are described in detail in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_.

.. note:: There is currently NO validation of user input in the website. Settings are validated by the device, but if invalid settings are sent to the device, there is no feedback to the user in the website at this time.

To change settings:

1) Navigate to the desired page
2) Edit the settings
3) Click the "Update" button

**Example**

.. figure:: images/ZLweb-config1.png
    :width: 550px

    **Select COM1 Configuration Page**

|

.. figure:: images/ZLweb-config2.png
    :width: 550px

    **Change Baud Rate to 19200**

|

.. figure:: images/ZLweb-config3.png
    :width: 550px

    **Click Update to Apply**

.. note:: Use caution when changing settings that can affect connection to the device, particularly those in Network or Radio Settings pages. Changes are applied immediately upon clicking the Update button.

.. _website-web-cli:

Web CLI
-------
The Z9-PE includes a Web API that provides access to CLI commands via an HTTP query string.

The general form of the API usage is as follows:

`http://<IP Address>/cli/<CLI Command>`

* The CLI Command after "http://<IP Address/cli/" is identical to a CLI command one would type in at the CLI prompt.
* The Z9-PE response will be in JSON format (See dumpFormat=Json on the System Commands page)

**NOTE:** You will need to authenticate with the web server using basic authentication to get access to the Web CLI. All web access uses GET methods, even those used to change device state.

Examples
~~~~~~~~

.. figure:: images/ZLwebCLIpic1.png
    :width: 550px

    **Get page list**

|

.. figure:: images/ZLwebCLIpic2.png
    :width: 550px

    **Get System Info**

|

.. figure:: images/ZLwebCLIpic3.png
    :width: 550px

    **Get txPower**

|

.. figure:: images/ZLwebCLIpic4.png
    :width: 550px

    **Set txPower**
