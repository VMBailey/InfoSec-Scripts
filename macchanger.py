#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/9/2023
# Purpose:          This script will chnage the MAC address of a Linux machine.

import subprocess

interface = input("Which interface would you like to change? ")
newMac = input("What MAC address would you like to assign to this device? ")

print("[+] Changing the MAC address for " + interface + " to " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + "wlan0 up", shell=True)