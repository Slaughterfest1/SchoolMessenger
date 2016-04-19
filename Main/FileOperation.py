
def saveMessage(fromUserName, toUserName, message):
    open("userMessages.txt", 'w').write(fromUserName + ":" + toUserName + ":" + message)


def findMessage(username):
    for fileline in open("userMessages.txt", "r"):
        linesplit = fileline.split(":")

        # Check for a username match
        if username == linesplit[0]:
            return linesplit[1], linesplit[2]

def saveRegistration(username, password):
    open("userRegistrations.txt", "w").write(username + ":" + password )

