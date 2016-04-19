import socket

class Driver:

    # Create a welcome socket bound at serverPort
    serverPort = 12009
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(10)

#Wait for incoming connection
while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()

   #Start thread upon accepting a connection
    ct = client_thread(clientsocket)
    ct.run()


#Save started thread into array of threads

#Pass the connection socket to the new thread

