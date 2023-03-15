#!/usr/bin/env python3

# Script Name:      MAC Address Changer
# Author:           Vincent Bailey
# Last Rev:         03/14/2023
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
#new_mac = input("What MAC address would you like to assign to this device? ")
#interface = options.interface
#new_mac = options.new_mac

##############################################################################
# Change MAC Function
##############################################################################
def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)

    # By enclosing our linux commands in quotations, this will prevent a user
    # from using any other linux commands while inputting their variables.
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

##############################################################################
# Get Arguments Function
##############################################################################
def get_arguments():
    # This variable contains the OpttionPArser class which allows us to add help
    # options should the user type "python macchanger.py --help" into their terminal.
    parser = optparse.OptionParser()

    # These variable lay out every option for our help menu.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Your MAC address of choice.")

    # By changing this variable from (options, arguments) = get_arguments() to 
    # a return statement, this tells python to return any variables that are
    # stored within parser.parse_args() any time this function is called.
    # return parser.parse_args()
    (options, arguments) = parser.parse_args()

    if not options.interface:
        # code to handle error
        parser.error("Please specify an interface. use -- help for more info.")
    elif not options.new_mac:
        # code to handle error
        parser.error("Please specify a valid MAC address. use -- help for more info.")
    return options

##############################################################################
# Main
##############################################################################
options = get_arguments()
change_mac(options.interface, options.new_mac)