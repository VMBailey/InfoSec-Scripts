#!/usr/bin/python3

# Script Name:      Packet Sniffer
# Author:           Vincent Bailey
# Last Rev:         04/18/2023
# Purpose:          This script will fetch packets from a network.


##############################################################################
# Libraries
##############################################################################
import scapy.all as scapy
from scapy.layers import http


##############################################################################
# Sniff Function
##############################################################################
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


##############################################################################
# Packets Sniffed Function
##############################################################################
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


##############################################################################
# Main
##############################################################################
sniff("eth0")


##############################################################################
# End
##############################################################################