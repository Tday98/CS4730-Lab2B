from socket import *
serverName = "192.168.0.52"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Programmer name: Tristan Day")
message = input("Input lowercase sentence and the server will make it into a title! ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()