import socket
import threading
import os.path

class Driver(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("(NEW THREAD) for IP: " + ip + ", Port = " + port)


def run(self, socket):
    self.socket.send("You are connected!".encode())


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


def savemessage(fromUserName, toUserName, message):
    filename = toUserName + ".txt"
    open(filename).write(toUserName + ":" + fromUserName + ":" + message)

def findmessage(username):
    filename = username + ".txt"
    for fileline in open(filename + ".txt", "r"):
        linesplit = fileline.split(":")
        # Check for a username match
        if username == linesplit[0]:
            return username, linesplit[1], linesplit[2]


def saveregistration(list):
    username = list[0]

    if userisregistered(username):
        return False

    password = list[1]
    firstname = list[2]
    lastname = list[3]
    email = list[4]

    # Create new file for user
    filename = username + ".txt"
    file = open(filename, 'w')

    #Save registration information
    file.write( username + ":" + password + ":" + firstname + ":" + lastname + ":" + email)
    return True

def userisregistered(username):
    filename = username + ".txt"
    return os.path.isfile(filename)



#Pass the connection socket to the new thread

