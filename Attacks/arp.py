import scapy.all as scapy
import subprocess
import sys
import re

opt_ip = ""


def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #Creates a request with that IP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast mac address
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #Lists that gave a response


    #Printing them out
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for element in answered_list:
        try:
            print(element[1].psrc + "\t\t" + element[1].hwsrc)
        except:
            print("That didn't work as expected!\n")


def main():
    global opt_ip
    if opt_ip != "":
        opt_ip = opt_ip[::-4]
        scan(str(opt_ip))
    else:
        scan("")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        opt_ip = sys.argv[1]
    main()