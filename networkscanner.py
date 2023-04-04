#!/usr/bin/env python3

# Script Name:      Network Scanner
# Author:           Vincent Bailey
# Last Rev:         04/4/2023
# Purpose:          This script will scan a subnet range using Scapy.

##############################################################################
# Libraries
##############################################################################
import scapy.all as scapy
import argparse


##############################################################################
# Scan Function
##############################################################################
def scan(ip):
    # This line searches for the IP address range on a network.
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()  # shows packet details

    # This line searches for the MAC address field on a network.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()  # shows packet details

    # scapy allows us to append both of the variables above with the line below.
    arp_request_broadcast = broadcast / arp_request

    # this line will send and receive packets using scapy's "srp" method.
    # srp abbreviated for "send / receive packets"
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # The print statement below allows us to create a small menu to display our
    # data. \t will tab spaces between strings while \n creates a new line.
    print ("IP\t\t\tMAC Address\n-----------------------------")
    client_list = []
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dict)
        print("-----------------------------------------------------")
    return client_list


##############################################################################
# Get Arguments Function
##############################################################################
def get_arguments():
    # The variable below contains the OptionParser class which allows us to add
    # descriptions to our -i and -m commands should the user type
    # "python3 macchanger.py --help" into their terminal.
    parser = argparse.ArgumentParser()

    # These variable lay out every option for our help menu.
    parser.add_argument("-t", "--target", dest="target", help="This is the subnet range that you wish to target.")

    # By changing this variable from (options, arguments) = get_arguments() to 
    # the line below, this tells python to store any arguments placed in the
    # terminal into the "options" variable.
    options = parser.parse_args()

    if not options.interface:
        # code to handle error
        parser.error("Please specify a subnet range. use --help for more info.")

    return options


##############################################################################
# Print Result Function
##############################################################################
def print_result(result_list):
    print ("IP\t\t\tMAC Address\n-----------------------------")
    for client in result_list:
        print(client["IP"] + "\t\t"+ client["MAC"])


##############################################################################
# Main
##############################################################################
scan_result = scan("Enter subnet range here")
print_result(scan_result)
# example: scan("10.0.2.1/24")
##############################################################################
# End
##############################################################################
