# Make a cuncurrent server receiving a text from another processes
from pickle import TRUE
from EchoServerClass import EchoServer
import time
import threading

serverPort = 12001         # Port to listen on (non-privileged ports are > 1023)
serverHost = "127.0.0.1"   # standard loop back interface address (localhost)


serverObject = EchoServer(serverHost,serverPort)
serverObject.Start()


# start server in a new threat. 

"""def startlisteningInNewThread():
    serverObject = EchoServer(serverHost,serverPort)
    serverObject.Start()

while True:
    serverObject = EchoServer(serverHost,serverPort)
    serverObject.Start()
"""

    


#while True:
#    counter = 0
#    print("Waiting for client to connect" + str(counter+1))
#    time.sleep(2) 