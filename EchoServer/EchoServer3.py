import socket
from socket import *
import threading
from RequestParser import parseRequest

# Make a server receiving a text from another program

serverPort = 12000         # Port to listen on (non-privileged ports are > 1023)
serverHost = "127.0.0.1"   # standard loop back interface address (localhost)
""" 
def DoOperation(request):
    pr = parseRequest(request)
    pr.ParseRequest()
    operation = pr.GetOperation()
    content = pr.GetContent()
    if operation == "lower":
        return content.lower()
    elif operation == "upper":
        return content.upper()
"""
def ParseRequestMethod(request):
    request = request.decode()
    pr = request.split(" ", 1)
    print(pr)
    operation = pr[0]
    content = pr[1]
    if operation == "lower":
        return content.lower()
    elif operation == "upper":
        return content.upper()
    

def handleClient(connectionSocket, addr):
    print(f"Connected by {addr}")
    sentence = connectionSocket.recv(1024)
    print (sentence)
    print(f"receive data from {addr}: {sentence}")
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

# handle upper and lower case
def handleClient2(connectionSocket, addr):
    print(f"Connected by {addr}")
    sentence = connectionSocket.recv(1024)
    print (sentence)
    print(f"receive data from {addr}: {sentence}")
    capitalizedSentence = ParseRequestMethod(sentence)
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()    

serverSocket = socket(AF_INET, SOCK_STREAM)   # IPV4 socket of TCP stream type.
serverSocket.bind((serverHost, serverPort))
serverSocket.listen()
print("server is ready to connect")


while True: 
    connectionSocket, addr = serverSocket.accept()
    #handleClient(connectionSocket, addr)
    #threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
    threading.Thread(target=handleClient2, args=(connectionSocket, addr)).start()



