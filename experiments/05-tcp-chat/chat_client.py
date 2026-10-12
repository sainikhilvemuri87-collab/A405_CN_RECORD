import socket
import threading

HOST = "127.0.0.1"
PORT = 2000

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print("\nServer:", data.decode(errors="replace"))
        except OSError:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    while True:
        message = input("Client: ")
        try:
            client.sendall(message.encode())
        except OSError:
            break
        if message.lower() == "exit":
            break
