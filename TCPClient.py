from socket import *
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
value = 'Y'
print("Programmer name: Tristan Day")
while value == 'Y':
    sentence = input("Input lowercase sentence and the server will turn it into a title! ")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From Server: ", modifiedSentence.decode())
    value = input("Keep going? (Y or N)").upper()
    if value == 'N':
        break
    while value != 'Y':
        value = input("Try again (Y or N)").upper()
        if value == 'N':
            break
clientSocket.close()