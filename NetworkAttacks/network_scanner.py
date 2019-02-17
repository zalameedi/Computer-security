#! usr/bin/env python



# Programmer: Zeid Al-Ameedi
# Date 02/17/2019
# Details: Code that uses module netifaces to access and get back your mac/ip address if an interface is specified.
# Possible that a machine might have more than one address. Thus we loop through ni.interfaces() and access the AF_LINK/
# AF_INET method which is a list of dictionaries to grab all the neccessary addresses.


import scapy.all as scapy
import netifaces as ni 
import os
import sys
import optparse



def scan(ip):
    scapy.arping(ip)

def get_AllmacAddr():
    for i in ni.interfaces(): 
        addr = ni.ifaddresses(i)
        print(addr[ni.AF_LINK][0]['addr']) # Mac addresses on network

def get_AllipAddr():
    for i in ni.interfaces():
        ip = ni.ifaddresses(i)[ni.AF_INET][0]['addr']
        print(ip)

def getIP():
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    return ip 

def getMac():
    mac = ni.ifaddresses(interface)[ni.AF_LINK][0]['addr']
    return mac

def main():
    global interface

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network interface to extract IP & mac addr")
    (options, par) = parser.parse_args()
    if not options.interface:
        print("[+] Mac Addresses \n")
        get_AllmacAddr()
        print("\n[+] IP Addresses \n")
        get_AllipAddr()
    else:
        interface=options.interface
        print("\n[+] IP Address \n")
        i = getIP()
        print(i)
        print("\n[+] Mac Address \n")
        m = getMac()
        print(m)


if __name__ == '__main__':
    main()



