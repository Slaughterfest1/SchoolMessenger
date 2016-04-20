import socket
import threading
import os.path
import time
import pickle


class DriverThread(threading.Thread):

    def __init__(self, new_socket):
        threading.Thread.__init__(self)
        self.socket = new_socket
        print("(NEW THREAD)")
        # self.username_list = [f for f in listdir(os.getcwd()) if isfile(join("stuff", f))]

    def run(self):

        while(1):
            response = self.socket.recv(1024).decode()
            print(response)

            # unpickle list and print it
            list_string = self.socket.recv(1024)
            test_list = pickle.loads(list_string)

            if "registration" in test_list[0]:
                username = test_list[1]

                password = test_list[2]
                firstname = test_list[3]
                lastname = test_list[4]
                email = test_list[5]

                # Create new file for user
                filename = username + ".txt"
                file = open(filename, 'w')

                # Save registration information
                file.write(username + ":" + password + ":" + firstname + ":" + lastname + ":" + email)
                return True
            
        print("Thread ended")

    def save_message(from_user, to_user, message):
        filename = to_user + ".txt"
        open(filename).write(to_user + ":" + from_user + ":" + message)


    def find_message(username):
        filename = username + ".txt"
        for fileline in open(filename + ".txt", "r"):
            line_split = fileline.split(":")
            # Check for a username match
            if username == line_split[0]:
                return username, line_split[1], line_split[2]


    def save_registration(info_list):
        username = info_list[1]

        if user_is_registered(username):
            return False

        password = info_list[2]
        firstname = info_list[3]
        lastname = info_list[4]
        email = info_list[5]

        # Create new file for user
        filename = username + ".txt"
        file = open(filename, 'w')

        # Save registration information
        file.write(username + ":" + password + ":" + firstname + ":" + lastname + ":" + email)
        return True

    def add_friend(user_adding, user_added):
        filename = user_adding + "friends.txt"
        file = open(filename, 'w')

        file.write(user_added) + ":"
        return True

    def get_friends(username):
        friends_file = open(username + "friends.txt", "r")
        friends = friends_file.read().split(':')

        return friends
              
def user_is_registered(username):
    # Get current folder
    curr_dir = os.getcwd()
    print("Current directory = " + curr_dir)

    filename = username + ".txt"
    print(os.path.isfile(filename))
    return os.path.isfile(filename)


serverport = 12009
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
serverSocket.bind(('', serverport))

threads = []
# Wait for incoming connections
while 1:
    serverSocket.listen(10)
    print("(DRIVER) Waiting for connection...")

    newsocket, address = serverSocket.accept()
    print("(DRIVER) Connection started...")

    # Create new thread for new connection
    thread = DriverThread(newsocket)
    thread.start()

    # Save started thread into array of threads
    threads.append(thread)

# Pass the connection socket to the new thread
