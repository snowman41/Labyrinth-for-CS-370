# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:56:20 2019

@author: bharr
"""

import socket
from _thread import *
import sys

def establish_connection(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), port))
    except:
        print()
    try:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
    except:
        print()