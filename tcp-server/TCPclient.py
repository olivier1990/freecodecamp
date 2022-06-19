# !/usr/bind/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.0.21'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.0.21', port))

#maximum data we allow coming to the port
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
