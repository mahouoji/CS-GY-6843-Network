#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    host = 'localhost' # socket.gethostname()
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() # Accept a connection
        try:
            message = connectionSocket.recv(4096) # Receive data from the socket
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read() # Read file
            print(outputdata)

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('HTTP/1.0 200 OK\n'.encode())
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('HTTP/1.0 404 Not Found\n'.encode())
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
