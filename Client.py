# ===================================
# HelloNameClient.py
# Written by:   Jeremy Bernien
# Written for:  Hello Name project
# Created on:   3/1/2016
# ===================================


def login_user():
    name = input("Please enter your user name:")
    # Try to log into the system using this name input
    loginMessage = "Login|" + name + "\r \n"
    print("Sent out:", loginMessage)
    clientSocket.send(loginMessage.encode())

    # Wait for the response from the server
    response = clientSocket.recv(1024).decode('ascii')

    print("Server Response:", response)
    if "200" in response:
        pswd = input("Please enter your password: ")
        clientSocket.send(pswd.encode())

    # Get login status from server
    newresponse = clientSocket.recv(1024).decode('ascii')
    loginStatus = newresponse.split('|')[1].strip()

    print("Login status is: ", loginStatus)
    # If loginStatus is success, ask user to generate report or quit
    if "SUCCESS" in loginStatus.upper():
        # Return to menu to ask user if they want to print their report
        return True
    else:
        return False


def register_user():
    newUsername = input("New username: ")
    registrationMessage = "Register|" + newUsername
    clientSocket.send(registrationMessage.encode())

    # Wait for ready message
    if "Ready" in clientSocket.recv(1024).decode('ascii'):

        # Get info from user and send to server
        password = input("Password: ")
        fullname = input("Full name: ")
        email = input("EmailAddress: ")
        registration = password + ":" + fullname + ":" + email
        clientSocket.send(registration.encode())

        # Check if registration was ok
        serverMsg = clientSocket.recv(1024).decode('ascii')
        print(serverMsg)
        if good_code(serverMsg):
            print("You are now able to log in.\n")
            return True
        else:
            return

    else:
        print("No response from the server")

def good_code(message):
    parts = message.split("|")
    if "CODE:404" in parts[0]:
        return False
    else:
        return True

from socket import *
# Create a socket and connect with the server
serverName = "172.20.73.151"  # Change it if you are running server elsewhere
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Send a hello message to the server
outgoing1 = "Hello"
clientSocket.send(outgoing1.encode())

# Wait the response from the server
incoming1 = clientSocket.recv(1024).decode('ascii')
print("Response: ", incoming1)

if "Hello" in incoming1:
    choice = 0
    while choice != 3:
        # Get name input from keyboard and send it to the server
        print("\nWhat would you like to do? \n1) Login \n2) Register a new username \n3) Exit ")
        choice = int(input("Choice: "))

        # User login method
        if choice == 1:
            if login_user() is not False:
                print("You are now logged in. Would you like to: \n1) Get your report \n2) Log off")
                answer = int(input())
                if answer == 1:
                    reportmsg = "REPORT|Please"
                    clientSocket.send(reportmsg.encode())

                    # Get success/failure message for finding record
                    foundReport = clientSocket.recv(1024).decode('ascii')
                    print(foundReport)

                    # If server returns a good code, wait for report to follow
                    if good_code(foundReport):
                        report = clientSocket.recv(1024).decode('ascii')
                        print(report)

        # User registration method
        elif choice == 2:
            register_user()

        elif choice == 3:
            print("\nGoodbye.")
        else:
            print("\nChoice not acceptable.")

clientSocket.close()





















