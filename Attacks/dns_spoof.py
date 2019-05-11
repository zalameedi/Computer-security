import subprocess
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()

def main():
    opt = 3
    try:
        while True:
            print("Run script on Host [1] or Victim [2] ?")
            opt = input()
            if (opt == 1):
                subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
                subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
                break
            elif (opt == 2):
                subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
                break
            else:
                continue
        
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet) #Connect it to your queue ID and callback function
        queue.run()
    except(KeyboardInterrupt):
        subprocess.call("iptables --flush", shell=True)


if __name__ == '__main__':
    main()