# !/usr/bind/python3

# Imported the socket module from the python standard library
import socket

# Specified socket family & socket type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.0.21'
host = socket.gethostname()

port = 444
# Bind host & port to the serversocket 
serversocket.bind(('192.168.0.21',port)) # Host will be replaced/substitued with IP, if changed and not running host

# listen(3) max computers that can connect to server
serversocket.listen(3)

while True:
    # information we accepted from the client (clientsocket, address)
    clientsocket, address = serversocket.accept()

    # message when client connects ("received connection from" & convert address to a string)
    # %s denotes a string conversion, %r will not be printed into the form of one data type
    print("received connection from: %s " % str(address))

    # Message to client + next paragraph
    message ='Hello, thank you fo connecting to the server. This is an example of how sockets can be used' + "\r\n"
    
    # Sending message to client
    clientsocket.send(message.encode('ascii'))
    
    # Close socket
    clientsocket.close()
