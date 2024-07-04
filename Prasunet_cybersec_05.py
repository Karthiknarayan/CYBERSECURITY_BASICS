from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Determine the protocol
        if protocol == 6:
            proto = "TCP"
        elif protocol == 17:
            proto = "UDP"
        else:
            proto = "Other"

        # Print packet details
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto}")
        
        # Check if the packet has a TCP/UDP layer and print payload
        if proto == "TCP" and TCP in packet:
            print(f"Payload: {packet[TCP].payload}")
        elif proto == "UDP" and UDP in packet:
            print(f"Payload: {packet[UDP].payload}")

        print("\n" + "-"*50 + "\n")

def main():
    # Capture packets
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
    #simply to check