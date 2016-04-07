import socket
from datetime import datetime

# Validates a user's information
# @Args: file = text file as a string
#        info = user's registration info from client
# @Return: returns validation message( "Success", or Error message )


# Server program.
# Protocol: to connect, send string "SuperSecretHandshake"
# Confirmation of handshake is "Success\tYour name:"

# Create a welcome socket bound at serverPort
serverPort = 12009
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)

print('The Hello Name server is ready to receive')
accessTime = datetime.now()
print("Access time is: ", accessTime)
read_file = open("tst.txt")


def validateuser(file, username, info):
    # Split user's info up into parts
    infosplit = info.split(":")
    passwrd = infosplit[0]
    fullname = infosplit[1]
    emailaddr = infosplit[2]

    # If the password is less than 6 chars then it's bad
    if len(passwrd) < 6:
            return "Password is too short."

    # Search each registered user for a match
    for fileline in open(file):
        linesplit = fileline.split(":")

        # Check for a username match
        if username == linesplit[0]:
            return "Username already exists"

        # Check if a registered user has the same name and email
        elif (fullname == linesplit[2]) and (emailaddr == linesplit[3]):
            return "Email address and full name is already a registered user"

    # Else the info meets all requirements
    return "Success"

# Starts the registration of a user, starting with their username
def register_user(newUsername):
    # Request the client's new registration info:

    registerMsg = "Ready for your data: \n"
    connectionSocket.send(registerMsg.encode())

    # Wait for user's information
    info = connectionSocket.recv(1024).decode('ascii')

    # Check to make sure username and info is unique
    success = validateuser("UserProfile.txt", newUsername, info)
    if success.upper() == "SUCCESS":
        # If successful, then register the user by writing it to file
        infoSplit = info.split(":")
        fullName = infoSplit[0]
        emailAddr = infoSplit[1]
        newpassword = infoSplit[2]

        open("UserProfile.txt", 'w').write(newUsername + ":" + fullName + ":" + emailAddr + ":" + newpassword)

        # Return a success message back to the client
        successRegMsg = "User succesfully registered."
        message_good(successRegMsg)
    else:
        errorRegMsg = "User was not registered. " + "(" + success + ")"
        message_bad(errorRegMsg)


# Begins login of a user, starting with their username
def login_user(userName):
    # Check whether this username is registered or not
    print("Check if one is registered or not....")

    loginStatus = "Failure"
    for line in open("UserProfile.txt", 'r'):
        registeredName = line.split(":")[0].strip()
        # If userName is a registered user, check their password
        if userName == registeredName:
            askpassword = "Please give the password for " + userName + ":"
            message_good(askpassword)

            # Check password from user
            password = connectionSocket.recv(1024).decode('ascii')
            registeredpwd = line.split(":")[1].strip()

            if registeredpwd == password:
                loginStatus = "Success. Login granted."
            else:
                loginStatus = "Failure. Password is incorrect."

    # If login is successful, record this access
    print("Login Status: ", loginStatus)
    if "Success" in loginStatus:
        accessTime = datetime.now()
        stringAccessTime = accessTime.strftime('%m/%d/%Y %H:%M:%S')
        print("Access time is", stringAccessTime)
        # Prepare the access record with information separated by tab key
        accessRecord = userName + "\t" + addr[0] + "\t" + stringAccessTime + "\n"
        # Append the access record into accessRecord.txt
        output_file = open("accessRecord.txt", "a")
        output_file.write(accessRecord)
        output_file.close()

    # Send out the login status response back to the client
    returnMessage2 = loginStatus

    if "Failure" in loginStatus and "Password" not in loginStatus:
        loginStatus = "Failure. That username has not been registered."
        message_bad(loginStatus)
    elif "Failure" in loginStatus and "Password" in loginStatus:
        message_bad(returnMessage2)
    print("Return to client:", returnMessage2)

    if "Success" in loginStatus:
        # Send good login message back
        message_good(returnMessage2)

        # Wait for the report request
        reportRequest = connectionSocket.recv(1024)
        print("From ", addr, reportRequest.decode('ascii'))
        if "REPORT" in reportRequest.decode('ascii').upper():
            find_records(userName)


def find_records(userName):
    # returnMessage3 = "\r \n"
    print("Searching for records for " + userName)
    # Open the access record file to find records for this client
    foundTag = False    # Tag for tracking records found or not
    completeRecord = ""
    for line in open("accessRecord.txt"):
        if userName in line:  # found the username in this record
            completeRecord += line
            if foundTag == False:      # Send out a Success message
                foundTag = True
                print("Report for ", userName, "\n", line)

    if foundTag:
        sucmessage = "Success. Found record."
        message_good(sucmessage)
        connectionSocket.send(completeRecord.encode())  # send all records to the client

    # If no record found, just send a failure message
    if foundTag == False:
        returnMessage3 = "Failure"
        message_bad(returnMessage3)


def message_good(message):
    okmessage = "CODE:200"
    fullmessage = okmessage + "|" + message
    connectionSocket.send(fullmessage.encode())


def message_bad(message):
    badmessage = "CODE:404"
    fullmsg = badmessage + "|" + message
    connectionSocket.send(fullmsg.encode())


while 1:
    connectionSocket, addr = serverSocket.accept()
    # Wait for the hello message
    sentence1 = connectionSocket.recv(1024)
    print("From", addr, sentence1.decode('ascii'))

    # Ask for name if a hello message is received
    if sentence1.decode('ascii').upper() == "HELLO":
        connectionSocket.send("Hello.\nPlease give me your command and info: ".encode())

    # Wait for the login message
    sentence2 = connectionSocket.recv(1024).decode('ascii')
    print(sentence2)
    parts = sentence2.split("|")
    methodName = parts[0].strip()
    otherInfo = parts[1].strip()

    print("From ", addr, methodName)

    # Check if method is to register a new account
    registerSuccess = False
    if methodName.upper() == "REGISTER":
        register_user(otherInfo)

    # Make sure it's a login message
    if methodName.upper() == "LOGIN":
        # Log user in, get login status
        status = login_user(otherInfo)

    connectionSocket.close()




