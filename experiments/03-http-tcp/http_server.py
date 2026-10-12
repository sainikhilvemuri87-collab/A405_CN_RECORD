import socket

HOST = "127.0.0.1"
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"HTTP server listening on http://{HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        request = conn.recv(4096).decode("utf-8", errors="replace")
        print("Received request:")
        print(request)
        body = "<html><body><h1>Welcome to Computer Networks Lab!</h1></body></html>"
        response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n" + f"Content-Length: {len(body.encode('utf-8'))}\r\nConnection: close\r\n\r\n" + body)
        conn.sendall(response.encode("utf-8"))
