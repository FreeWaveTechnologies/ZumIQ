''' Demonstration of using the Web CLI programmatically for device configuration

    This code was developed on Python 3.4 but should run on Python 2.7
'''

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
