import socket
from socket import *

# Make a server receiving a text from another program

serverPort = 12005         # Port to listen on (non-privileged ports are > 1023)
serverHost = "127.0.0.1"   # standard loop back interface address (localhost)

serverSocket = socket(AF_INET, SOCK_DGRAM)   # IPV4 socket of UDP stream type.
serverSocket.bind(('', serverPort))
print("server is ready to connect")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Connected by {clientAddress}")
    sentence = message.decode()
    print (sentence)
    capitalizedSentence = sentence.upper()
    serverSocket.sendto(capitalizedSentence.encode(), clientAddress)
   

