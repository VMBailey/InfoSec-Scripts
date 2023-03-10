#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/9/2023
# Purpose:          This script will chnage the MAC address of a Linux machine.

import subprocess
import optparse

# This variable contains the OpttionPArser class which allows us to add help
# options should the user type "python macchanger.py --help" into their terminal.
parser = optparse.OptionParser()

# This variable lays out every option for our help menu.
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")

# This variable helps to understand the options added into the "add_option" method.
parser.parse_args()

interface = input("Which interface would you like to change? ")
newMac = input("What MAC address would you like to assign to this device? ")

print("[+] Changing the MAC address for " + interface + " to " + newMac)

# By enclosing our linux commands in quotations, this will prevent a user
# from using any other linux commands while inputting their variables.
subprocess.call(["ifconfig ", interface, " down"])
subprocess.call(["ifconfig ", interface, " hw", "ether", newMac])
subprocess.call(["ifconfig ", interface, " up"])