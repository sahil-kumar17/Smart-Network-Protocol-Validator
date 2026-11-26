import socket

HOST, PORT = "0.0.0.0", 8080   # 0.0.0.0 = network ke saare interfaces par sunna

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"Server sun raha hai port {PORT} par...")
    while True:
        conn, addr = srv.accept()
        print("Connected:", addr)       # addr = (client IP, client port)
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Mila:", data.decode(errors="ignore"))
                conn.sendall(b"OK: " + data)
        print("Disconnected:", addr)