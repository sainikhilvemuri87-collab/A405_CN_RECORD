import socket

hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address = "Unable to resolve hostname"

print("Hostname:", hostname)
print("IP Address:", ip_address)
