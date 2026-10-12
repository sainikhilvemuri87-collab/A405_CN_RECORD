import socket

HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        message = input("Enter message (exit to quit): ")
        client.sendall(message.encode())
        if message.lower() == "exit":
            break
        print("Echoed from server:", client.recv(1024).decode(errors="replace"))
