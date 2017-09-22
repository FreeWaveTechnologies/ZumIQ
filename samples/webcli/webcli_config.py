''' Demonstration of using the Web CLI programmatically for device configuration

    This code was developed on Python 3.4 but should run on Python 2.7
'''

# ----------------------------------------------------------------------------
# BSD 2-Clause License
#
# Copyright (c) 2017, FreeWave Technologies
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import requests

IP_ADDRESS = '192.168.111.100'
USERNAME = 'admin'
PASSWORD = 'admin'
BASE_URL = 'http://{}/cli/'.format(IP_ADDRESS)

def main():
    """ Execute all of the demos """

    print("########## Show All Pages ##########")
    show_pages()

    print("########## Show System Info Page ##########")
    show_systeminfo()

    print("########## Show Transmit Power ##########")
    show_txpower()

    print("########## Change Transmit Power ##########")
    change_txpower()

def show_pages():
    """ Demonstrates retrieving the list of all CLI pages """

    pages_response = webcli_command('pages')
    for page in pages_response:
        print(page)


def show_systeminfo():
    """ Demonstrates retrieving the contents of the 'systemInfo' page """

    systeminfo_response = webcli_command('systemInfo')
    for key, value in systeminfo_response['systemInfo'].items():
        print('{}={}'.format(key, value))


def show_txpower():
    """ Demonstrates retrieving the transmit power value """

    txpower_response = webcli_command('radioSettings.txPower')
    value = txpower_response['radioSettings']['txPower']
    print(value)


def change_txpower():
    """ Demonstrates changing the transmit power """

    txpower_response = webcli_command('radioSettings.txPower')
    current_txpower = txpower_response['radioSettings']['txPower']
    print("Current Transmit Power: " + current_txpower)

    # rudimentary check to ensure we're actually making a change
    new_txpower = '10dbm'
    if current_txpower == '10dbm':
        new_txpower = '12dbm'

    change_txpower_response = webcli_command('radioSettings.txpower=' + new_txpower)
    changed_txpower = change_txpower_response['radioSettings']['txPower']
    print("Changed Transmit Power: " + changed_txpower)


def webcli_command(command):
    """ Helper function to execute a Web CLI command and return its response """

    req = requests.get(BASE_URL + command, auth=(USERNAME, PASSWORD))
    #print('HTTP Status: {}/{}'.format(req.status_code, req.reason))

    obj = req.json()[0]
    #print('CLI Status: {}/{}'.format(obj['RESULT']['RESULT'], obj['RESULT']['MESSAGE']))

    return obj['RESPONSE']['pages']


if __name__ == '__main__':
    main()
