''' Demonstration of using cliBridge programmatically for device configuration

    This code requires the use of Python 2.7
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
