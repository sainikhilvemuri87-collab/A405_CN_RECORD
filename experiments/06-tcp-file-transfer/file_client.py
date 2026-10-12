import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5001
SOURCE_FILE = Path("sample_file.txt")
if not SOURCE_FILE.exists():
    SOURCE_FILE.write_text("Computer Networks Lab TCP file transfer demo.\n", encoding="utf-8")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    with SOURCE_FILE.open("rb") as source:
        for data in iter(lambda: source.read(4096), b""):
            client.sendall(data)
    client.shutdown(socket.SHUT_WR)
print(f"Sent {SOURCE_FILE}")
