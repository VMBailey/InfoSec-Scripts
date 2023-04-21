#!/usr/bin/env python3

# Script Name:      Tip Calculator
# Author:           Vincent Bailey
# Last Rev:         04/20/2023
# Purpose:          This script will split a bill amongst a party of people.

##############################################################################
# Variables
##############################################################################
print("Welcome to the Tip Calculator! :D")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to add? 10, 12, 15? "))
split = int(input("How many people are you splitting the bill with? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

##############################################################################
# Main
##############################################################################
print(f"Each person should pay: ${final_amount}")