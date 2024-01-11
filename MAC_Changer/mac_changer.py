#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")

    return parser.parse_args()


def change_mac(interface : str, new_mac : str):
    print(f"[+] Changing MAC address for interface: {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])  # list calling instead of concatenations to avoid ; hijacking
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.newMac)

