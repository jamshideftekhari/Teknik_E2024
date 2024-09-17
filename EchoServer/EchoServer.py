import socket
from socket import *

# Make a server receiving a text from another program

serverPort = 12000         # Port to listen on (non-privileged ports are > 1023)
serverHost = "127.0.0.1"   # standard loop back interface address (localhost)

serverSocket = socket(AF_INET, SOCK_STREAM)   # IPV4 socket of TCP stream type.
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("server is ready to connect")

connectionSocket, addr = serverSocket.accept()
print(f"Connected by {addr}")
sentence = connectionSocket.recv(1024)
print (sentence)
capitalizedSentence = sentence.upper()
connectionSocket.send(capitalizedSentence)
connectionSocket.close()

