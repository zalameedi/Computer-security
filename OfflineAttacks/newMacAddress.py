#!/usr/bin/env python

# Programmer: Zeid Al-Ameedi
# Published 02-06-2018
# Details: Changes the mac address on a network interface card temporarily, 
#          for a higher level of anonymity. 
#          Works on UNIX operating systems.

#          Run with: python script.py <network interface>

import subprocess;
import os;
import sys;


def main():
    if len(sys.argv) < 2:
        print("Must pass the network interface.")
    else:
        global networkInterface
        networkInterface = sys.argv[1]
        change_mac()

def change_mac():
    subprocess.call("ifconfig {0} down".format(networkInterface), shell=True)
    newAddress = input("Enter new mac address in the form xx:xx:xx:xx:xx:xx [where x -> {0...9} ")
    subprocess.call("ifconfig {0} hw ether {1}".format(networkInterface, newAddress), shell=True)
    subprocess.call("ifconfig {0} up".format(networkInterface), shell=True)


if __name__ == '__main__':
    main()
