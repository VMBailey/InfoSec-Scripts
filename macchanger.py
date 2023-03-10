#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/9/2023
# Purpose:          This script will chnage the MAC address of a Linux machine.

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)