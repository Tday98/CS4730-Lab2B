from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Programmer name: Tristan Day")
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            break
        capitalizedSentence = sentence.title()
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()