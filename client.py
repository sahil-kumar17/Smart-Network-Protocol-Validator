import socket, sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 8080

with socket.create_connection((HOST, PORT), timeout=5) as s:
    s.sendall(b"hello from client")
    print(s.recv(1024).decode())