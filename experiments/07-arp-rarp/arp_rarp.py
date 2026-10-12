arp_table = {"192.168.1.1": "AA:BB:CC:DD:EE:01", "192.168.1.2": "AA:BB:CC:DD:EE:02", "192.168.1.3": "AA:BB:CC:DD:EE:03"}
print("ARP Simulation")
ip = input("Enter IP address: ").strip()
print("MAC address:", arp_table.get(ip, "No ARP entry found"))
print("\nRARP Simulation")
mac = input("Enter MAC address: ").strip().upper()
reverse_table = {v: k for k, v in arp_table.items()}
print("IP address:", reverse_table.get(mac, "No RARP entry found"))
