#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/11/2023
# Purpose:          This script will chnage the MAC address of a Linux machine.

##############################################################################
# Libraries
##############################################################################
import subprocess
import optparse

##############################################################################
# Global Variables
##############################################################################
#interface = input("Which interface would you like to change? ")
#new_Mac = input("What MAC address would you like to assign to this device? ")
#interface = options.interface
#new_Mac = options.new_Mac

##############################################################################
# Change MAC Function
##############################################################################
def change_Mac(interface, new_Mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_Mac)

    # By enclosing our linux commands in quotations, this will prevent a user
    # from using any other linux commands while inputting their variables.
    subprocess.call(["ifconfig ", interface, " down"])
    subprocess.call(["ifconfig ", interface, " hw", "ether", new_Mac])
    subprocess.call(["ifconfig ", interface, " up"])

##############################################################################
# Get Arguments Function
##############################################################################
def get_arguments():
    # This variable contains the OpttionPArser class which allows us to add help
    # options should the user type "python macchanger.py --help" into their terminal.
    parser = optparse.OptionParser()

    # These variable lay out every option for our help menu.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_Mac", help="Your MAC address of choice.")

    # By changing this variable from (options, arguments) = get_arguments() to 
    # a return statement, this tells python to return any variables that are
    # stored within parser.parse_args() any time this function is called.
    return parser.parse_args()

##############################################################################
# Main
##############################################################################
(options, arguments) = get_arguments()
change_Mac(options.interface, options.new_Mac)