#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/9/2023
# Purpose:          This script will chnage the MAC address of a Linux machine.

import subprocess

interface = "wlan0"
newMac = "00:11:22:33:44:66"

print("[+] Changing the MAC address for " + interface + " to " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + "wlan0 up", shell=True)