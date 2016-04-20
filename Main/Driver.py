import socket
import threading


class Driver(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("(NEW THREAD) for IP: " + ip + ", Port = " + port)

    def run(self, socket):
        print("")





    def main(self):
        serverport = 12009
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
        serverSocket.bind(('', serverport))

        threads = []
        # Wait for incoming connections
        while 1:
            serverSocket.listen(10)
            print("(DRIVER) Waiting for connection...")
            (newsocket, (ip, port)) = serverSocket.accept()

            # Create new thread for new connection
            thread = Driver(ip, port, newsocket)
            thread.start()

            # Save started thread into array of threads
            threads.append(thread)




#Pass the connection socket to the new thread

