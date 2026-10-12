import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5001
OUTPUT_FILE = Path("received_file.txt")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"File server listening on port {PORT}")
    conn, addr = server.accept()
    with conn, OUTPUT_FILE.open("wb") as output:
        print("Connected by", addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            output.write(data)
    print(f"File saved as {OUTPUT_FILE}")
