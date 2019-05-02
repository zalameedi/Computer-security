import scapy.all as scapy
import sys

#iface specifies interface, store (stores data in memory) prn is a callback function

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    print(packet)


def main():
    interface = ""
    if(len(sys.argv) >= 2):
        interface=sys.argv[1]
    sniff(interface)


if __name__ == '__main__':
    main()