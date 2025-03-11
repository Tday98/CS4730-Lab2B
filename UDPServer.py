from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("Server running on port " + str(serverPort))
print("Programmer name: Tristan Day")
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().title()
    serverSocket.sendto(modifiedMessage.encode(),  clientAddress)