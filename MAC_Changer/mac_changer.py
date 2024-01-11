#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for info.")  # paser.error exits the program
    elif not options.newMac:
        parser.error("[-] Please specify a new mac address, use -h or --help for info.")

    return options


def change_mac(interface : str, new_mac : str):
    print(f"[+] Changing MAC address for interface: {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])  # list calling instead of concatenations to avoid ; hijacking
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address, check interface and MAC validity")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print(f"Current MAC = {str(current_mac)}")

change_mac(options.interface, options.newMac)

current_mac = get_current_mac(options.interface)

if current_mac == options.newMac:
    print(f"[+] MAC address changed to {current_mac}")
else:
    print(f"[-] MAC address change failed")
