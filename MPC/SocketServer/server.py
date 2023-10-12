#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM

with socket.socket(IPV4, TCP) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)   
            try:    
                decoded_data = int(data.decode("utf-8"))
                decoded_data *= 2
                final_data = str(decoded_data).encode("utf-8")
                conn.sendall(final_data)
            except ValueError:
                break