import os.path

def saveMessage(fromUserName, toUserName, message):
    filename = toUserName + ".txt"
    open(filename).write(toUserName + ":" + fromUserName + ":" + message)


def findMessage(username):
    filename = username + ".txt"
    for fileline in open(filename + ".txt", "r"):
        linesplit = fileline.split(":")

        # Check for a username match
        if username == linesplit[0]:
            return username, linesplit[1], linesplit[2]

def saveRegistration(username, password):
    open("userRegistrations.txt", "w").write(username + ":" + password )

def userIsRegistered(username, password):
    filename = username + password + ".txt"
    os.path.isfile(filename)

def newUserfile(username):
    filename = username + ".txt"
    open(filename, 'w')
