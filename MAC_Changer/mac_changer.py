#!/usr/bin/env python

import subprocess

interface : str = str(input("Insert the interface to change: \n>> "))
newMac : str = str(input("Insert the new MAC address: \n>> "))

print(f"[+] Changing MAC address for interface: {interface} to {newMac}")

'''

#!-- Insecure version, can be hijacked with ; injections

subprocess.call(f"ifconfig {interface} down", shell=True) #eth0 for ether, wlan0 for wi-fi
subprocess.call(f"ifconfig {interface} hw ether {newMac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

'''
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",newMac])
subprocess.call(["ifconfig",interface,"up"])