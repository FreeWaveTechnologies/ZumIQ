''' Demonstration of using cliBridge programmatically for device configuration

    This code requires the use of Python 2.7
'''

import subprocess

def main():
    """ Prompt use and execute selected example """

    print('What do you want to do?')
    print('-----------------------')
    print('  1) Show System Info')
    print('  2) Read Transmit Power')
    print('  3) Change Transmit Power')

    choice = raw_input('Your choice [1-3]> ')

    if choice == '1':
        show_system_info()
    elif choice == '2':
        show_tx_power()
    elif choice == '3':
        change_tx_power()
    else:
        print('I\'m sorry, I didn\'t understand')

def show_system_info():
    """ Executes the command 'cliBridge systemInfo' and displays the result

        This demonstrates retrieving the contents of an entire page at once.
        The raw output of the command is displayed with no parsing.
    """
    system_info = subprocess.check_output(['cliBridge', 'systemInfo'])
    print(system_info)

def show_tx_power():
    """ Executes the command 'cliBridge radioSettings.txPower' and displays the result

        This demonstrates retrieving the contents of a single parameter
    """

    tx_power = read_setting_value('radioSettings.txPower')
    print(tx_power)


def change_tx_power():
    """ Executes the command 'cliBridge radiosettings.txPower=XXX and displays the result

        This demonstrates changing the value of a single parameter
    """
    current_tx_power = read_setting_value('radioSettings.txPower')

    # rudimentary check to ensure we're actually making a change
    new_tx_power = '10dbm'
    if current_tx_power == '10dbm':
        new_tx_power = '12dbm'

    print('Changing txPower from {} to {}'.format(current_tx_power, new_tx_power))

    write_setting_value('radioSettings.txPower', new_tx_power)


def read_setting_value(setting):
    """ Executes the command 'cliBridge <setting>' and parses the result.
        NOTE: 'setting' must be expressed as 'page.parameter' in this simplified example.

        This demonstrates getting the actual value from a command
    """
    response = subprocess.check_output(['cliBridge', setting])
    lines = response.splitlines()
    line = filter(lambda x: str(x).startswith(setting + '='), lines)[0]

    value = line.split('=')[1]

    return value


def write_setting_value(setting, value):
    """ Executes the command 'cliBridge <setting>=<value> """

    response = subprocess.check_output(['cliBridge', setting + '=' + value])


if __name__ == '__main__':
    main()
