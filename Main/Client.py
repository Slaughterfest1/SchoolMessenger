import socket
import time


home = "172.20.118.96"
port = 12009
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((home, port))

print("connected.")
while(1):
    time.sleep(10)
    client_socket.send("sent".encode())