import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555

s.bind((socket.gethostname(), port))
print(socket.gethostname())
s.listen(2)

while True: 
    clientsocket, address = s.accept()
    print(f"connection from {address} established.")
    clientsocket.send(bytes("Welcome to the Labyrinth server!" , "utf-8"))