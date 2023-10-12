#!/usr/bin/env python3
import socket
import sys

message = sys.argv[1:]
message = " ".join(message)


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode("utf-8"))
    print(f"Sent {message}")
    data = s.recv(1024)
    data = data.decode("utf-8")
    print(f"Received {data}")
