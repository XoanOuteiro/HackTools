#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

'''

    ---Definition of parser options

'''
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface : str = options.interface
newMac : str = options.newMac

'''

    ---Program logic

'''
print(f"[+] Changing MAC address for interface: {interface} to {newMac}")

subprocess.call(["ifconfig", interface, "down"])  # list calling instead of concatenations to avoid ; hijacking
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])