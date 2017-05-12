App Installation and Startup
============================
While there is no strict requirement that an app developer use the directory structure described in :doc:`Developer Environment`, this procedure allows for consistency of app deployment and allows FreeWave technical support to better help with app installation and operation issues.

Installation and Startup
------------------------
The basic procedure is:

1) Copy the app files to the device.
2) Move the app files to a subdirectory within */home/devuser/apps*.
3) Create or edit a **run** shell script with all the commands necessary to start the app.
4) Create a symlink in */home/devuser/service* linking to the subdirectory created in Step 2.

**Example**

To demonstrate, a simple Python *Hello World* web app running on the Flask web platform will be used.

.. note:: By default, Flask is included on the Z9-PE.

The file *hello.py* in this example contains the following code:

::

 from flask import Flask
 app = Flask(__name__)

 @app.route("/")
 def hello():
     return "Hello World!"

 if __name__ == "__main__"
     app.run(host='0.0.0.0')

Copy App Files to Device
------------------------
There are three ways to do this:

* **Option 1: PTP Drag-and-Drop Interface**
    - Uses the PTP Drag-and-Drop interface in Windows File Explorer (via USB connection).

.. note:: This is the **only** option if the Z9-PE has NOT been configured as a device on your network.

* **Option 2: Device Website**
    - Uses the file upload feature of the Z9-PE website.

* **Option 3: SCP**
    - Uses SCP to copy the files directly to the device.

Option 1: PTP Drag-and-Drop Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: The drag-and-drop interface is described in detail in the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_. This procedure describes basic operation.

1) Use the Micro USB port to connect the Z9-PE to a computer.
2) If drivers have not yet been installed, driver installation will start. You may be prompted to allow this to happen.
3) A ZumLink device will appear in your File Explorer with a camera icon.

.. note:: The Z9-PE uses PTP (Picture Transport Protocol) to copy files directly from Windows, hence the camera icon).

4) Open the ZumLink device. It wil contain a single folder with the device serial number as its name. Inside this folder are a number of configuration and informational files. See :ref:`ptp-directory-contents`

 .. figure:: images/ZLpic1.png

    **Z9-PE Configuration Files**

5) Drag-and-Drop or copy-and-paste the app file(s) into this folder (*hello.py* in this example).

.. note:: On Windows® 8 and later, you must append ".txt" to the filename to get around Windows driver issues. Be sure to remove this extension after copying.

.. figure:: images/ZLpic2.png

    **Drag-and-Drop the** *hello.py* **file**

6) The files(s) will now be available on the Z9-PE in the */ptp* directory.

.. figure:: images/ZLpic3.png

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/ptp$ <b>ls</b>
    boot_results.txt       fw_upgrade_result.txt   help.txt           modbuslayout.txt
    config.txt             hello.py.txt            layout.txt         sys_info.txt
    freewave-ib:/ptp$ <b>mv hello.py.txt hello.py</b>
    freewave-ib:/ptp$
    </pre>

**Option 2: Device Website**

1) Open a web browser.
2) In the URL address bar, enter the IP address of the attached Z9-PE.

.. note:: The default IP address of the Z9-PE is 192.168.111.100. See the `ZumLink Z9-PE User Manual <http://support.freewave.com/wp-content/uploads/DRAFT-LUM0076AA-ZumLink-Z9-PE-User-Manual-Rev-Oct-2016-v0.28.pdf>`_ for detailed instructions on how to configure the Z9-PE network settings.

3) Select the **File Upload** link.

.. figure:: images/ZLpic4.png

    **File Upload Link**

4) If prompted, login to the Z9-PE.
5) Click **Choose File** to select the file to upload.

.. figure:: images/ZLpic5.png

    **Choose File**

6) Select the file to upload.
7) Click "Send" to send the file to the device.

.. figure:: images/ZLpic6.png

    **Send File**

The file is now be available on the Z9-PE in the */ptp* directory:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/ptp$ <b>ls</b>
    boot_results.txt       fw_upgrade_result.txt   help.txt           modbuslayout.txt
    config.txt             hello.py                layout.txt         sys_info.txt
    freewave-ib:/ptp$
    </pre>

**Option 3: SCP**

This procedure assumes that you have the **scp** command line utility located in your path. scp is generally available on Linux systems by default. It can be installed on Windows (via CygWin or git, for example) but installation is left as an exercise to the user.

1) From a shell prompt in your desired shell, type:

	``scp myfile devuser@###.###.###.###:/ptp/myfile``

**Example:**

.. raw:: html

    <pre class="cmdline">
    C:\demo> <b>scp hello.py devuser@192.168.111.100:/ptp/hello.py</b>
    devuser@192.168.111.100's password:
    hello.py                                      100%  157     0.2KB/s   00:00
    C:\demo>
    </pre>

The file is now be available on the Z9-PE in the */ptp* directory:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/ptp$ <b>ls</b>
    boot_results.txt       fw_upgrade_result.txt   help.txt           modbuslayout.txt
    config.txt             hello.py                layout.txt         sys_info.txt
    freewave-ib:/ptp$
    </pre>

.. note:: Using SCP, developers are not limited to only using the */ptp* directory. Files can be copied directly to any location on the Z9-PE, including directly into */home/devuser/apps*.

.. _move-app-files-to-app-directory:

Move App Files to App Directory
-------------------------------
1) Login to the Z9-PE as **devuser**
2) Change directory to */home/devuser/apps*:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:~$ <b>cd /home/devuser/apps</b>
    freewave-ib:/home/devuser/apps$ <b>ls</b>
    template
    freewave-ib:/home/devuser/apps$
    </pre>

3) Create a directory to contain your app files, using the template directory at */home/devuser/apps/template*:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/home/devuser/apps$ <b>cp -r template HelloDemo</b>
    freewave-ib:/home/devuser/apps$ <b>cd HelloDemo</b>
    freewave-ib:/home/devuser/apps/HelloDemo$ <b>ls</b>
    run
    freewave-ib:/home/devuser/apps/HelloDemo$
    </pre>

4) Copy your app files into the new directory:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/home/devuser/apps/HelloDemo$ <b>cp /ptp/hello.py .</b>
    freewave-ib:/home/devuser/apps/HelloDemo$ <b>ls</b>
    hello.py run
    freewave-ib:/home/devuser/apps/HelloDemo$
    </pre>

Create or Edit "run" Script
---------------------------
Edit the *run* script to contain whatever commands are necessary to start the application.

.. note:: The "vi" editor is available on the Z9-PE.

.. raw:: html

    <pre class="cmdline">
    freewave-ib:~/apps/HelloDemo$ <b>vi run</b>
    </pre>

**Contents of** *run* **script after editing:**

::

 #!/bin/sh

 # start your app here
 python hello.py

If you create the *run* script from scratch, ensure that it is world-executable by using the **chmod** command:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/home/devuser/apps/HelloDemo$ <b>chmod 755 run</b>
    freewave-ib:/home/devuser/apps/HelloDemo$ <b>ls -l</b>
    -rw-r-----   1 devuser  devuser     171 Jan  1 03:07 hello.py
    -rwxr-xr-x   1 devuser  devuser      49 Jan  1 02:56 run
    freewave-ib:/home/devuser/apps/HelloDemo$
    </pre>

.. _create-symbolic-link:

Create Symbolic Link for Automatic Startup
------------------------------------------
1) Create a symbolic link in */home/devuser/service* pointing to the app directory created in :ref:`move-app-files-to-app-directory`:

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/mnt/user_data/HelloDemo$ <b>cd ../../service</b>
    freewave-ib:/home/devuser/service$ <b>ln -s /home/devuser/apps/HelloDemo HelloDemo</b>
    freewave-ib:/home/devuser/service$ <b>ls</b>
    HelloDemo
    freewave-ib:/home/devuser/service$
    </pre>

2) Verify the app is running using the ps command:

.. note:: The application should start automatically (a service monitors the service directory for new apps). It will start automatically when the device boots.

.. raw:: html

    <pre class="cmdline">
    freewave-ib:/home/devuser/service$ <b>ps</b>
    PID USER       VSZ STAT COMMAND
    4205 devuser   2728 S    {devuser_bash} /bin/sh /mnt/fw/bin/devuser_bash
    4208 devuser   3184 S N  /bin/bash
    4485 devuser   2724 S N  {run} /bin/sh ./run
    4486 devuser  15224 S N  python hello.py
    4494 devuser   2860 R N  ps
    freewave-ib:/home/devuser/service$
    </pre>

.. note:: There are two processes involved. One process executes the run script and another process executes the actual app.

3) In a web browser, got to "<IP address>:5000" to confirm that the demo app is performing as expected:

.. image:: images/ZLpic7.png

To stop an app that has been started automatically:

1) Remove the symbolic link created in :ref:`create-symbolic-link` (otherwise the app runner will just start the app again)

2) Kill the running processes or reboot the device.
