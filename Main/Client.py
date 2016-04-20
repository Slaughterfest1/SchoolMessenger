import socket
import time
import pickle


home = "192.168.1.4"
port = 12009
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((home, port))

print("connected.")
while(1):
    time.sleep(10)
    client_socket.send("sent".encode())
    test_list = ["registration", "dalyjw17", "password", "john", "daly", "dalyjw17@uww.edu"]
    pickled_string = pickle.dumps(test_list)
    client_socket.send(pickled_string)
