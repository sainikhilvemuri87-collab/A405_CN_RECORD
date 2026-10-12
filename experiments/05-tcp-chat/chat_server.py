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
            print("\nClient:", data.decode(errors="replace"))
        except OSError:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Chat server listening on {PORT}")
    conn, addr = server.accept()
    print("Connected by", addr)
    with conn:
        threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
        while True:
            message = input("Server: ")
            try:
                conn.sendall(message.encode())
            except OSError:
                break
            if message.lower() == "exit":
                break
