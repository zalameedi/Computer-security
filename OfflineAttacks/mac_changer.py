#! usr/bin/env python

# Script to change mac_address, difference being the cmd line options -i and -m

import subprocess
import optparse


def main():
    global interface
    global new_mac

    parser = optparse.OptionParser() #initialize instance of that object
    parser.add_option("-i", "--interface", dest = "interface", help="Network Interface to change the Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help = "Enter new mac address in form xx:xx:xx:xx:xx:xx")

    (options, args) = parser.parse_args()
    if not options.interface or not options.new_mac:
        print("Interface and new mac address must be given.")
    else:
        interface=options.interface
        new_mac=options.new_mac
        newMac()


def newMac():
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    print("[+] Mac Address successfully changed to {0}".format(new_mac))

if __name__ == '__main__':
    main()