import socket

hostname = socket.gethostname()
print("Hostname:", hostname)
try:
    ip_address = socket.gethostbyname(hostname)
    print("IP Address:", ip_address)
except socket.gaierror as error:
    print("Could not resolve hostname:", error)
try:
    with open("/etc/resolv.conf", "r", encoding="utf-8") as f:
        for line in f:
            fields = line.split()
            if fields and fields[0] == "nameserver":
                print("Configured DNS Server:", fields[1])
except OSError:
    print("DNS server configuration could not be read on this system.")
