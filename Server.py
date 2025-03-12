from socket import *
import sys # create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8080
# to use system functions
#Fill in your code for binding and keeping your socket ready to listen
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("Programmer Name: Tristan Day")
while True:
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()#Fill your code for accepting client connection
    print("Connection from", addr)
    try:
    # receive message request
        message = connectionSocket.recv(1024).decode()#Fill your code here
    #Extract the path of the requested object from the message
        if not message:
            connectionSocket.close()
            continue
        print(message)
    #The path is the second part of the HTTP header, identified by [1]
        filename = message.split()[1]
    #The extracted path of the HTTP requests include character ‘\’, so read
    #the path from the second character
        with open(filename[1:], "rb") as f:
            outputdata = f.read()
    #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n"
                              "Content-Type: text/html\r\n"
                              f"Content-Length {len(outputdata)}\r\n"
                              "\r\n".encode() + outputdata)
    #Send the content of the requested file to the client (connection socket)
    #close the client connection socket
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill your code here for the ‘404 Not Found’ message
        #Close client socket
        #Fill your code here
        outputdata = "<h1>404 Not Found</h1>"
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n"
                              "Content-Type: text/html\r\n"
                              f"Content-Length {len(outputdata)}\r\n"
                              "\r\n".encode() + outputdata.encode())
    finally:
        connectionSocket.close()
serverSocket.close()
sys.exit()