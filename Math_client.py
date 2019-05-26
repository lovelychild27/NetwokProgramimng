# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:06:34 2019

@author: My Computer
"""

from socket import *
from threading import Thread


def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        if msg == "{quit}":
            client_socket.close()
            break
        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            break


HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()