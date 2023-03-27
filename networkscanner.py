#!/usr/bin/env python3

# Script Name:      Network Scanner
# Author:           Vincent Bailey
# Last Rev:         03/27/2023
# Purpose:          This script will scan a subnet range using Scapy.

##############################################################################
# Libraries
##############################################################################
import scapy.all as scapy


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
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("-----------------------------------------------------")


##############################################################################
# Main
##############################################################################
scan("Enter subnet range here")
# example: scan("10.0.2.1/24")
##############################################################################
# End
##############################################################################
