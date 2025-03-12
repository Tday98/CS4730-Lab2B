from socket import *
import sys
clientSocket = socket(AF_INET, SOCK_STREAM)
serverName = sys.argv[1]
serverPort = sys.argv[2]
serverFile = sys.argv[3]
clientSocket.connect((serverName,int(serverPort)))
print("Programmer name: Tristan Day")
# Format should be client.py serverName serverPort serverFile in CLI
clientSocket.send((f"GET /{serverFile} HTTP/1.1\r\nHost:{serverName}\r\nConnection: close\r\n\r\n").encode())
reply = b""
while True:
    recw = clientSocket.recv(1024)
    if not recw:
        break
    reply += recw
print(reply)

clientSocket.close()