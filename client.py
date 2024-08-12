import socket

import sys
import os
import threading

from rsa import generateKey


nickname = input('Choose a nickname : ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4444))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "nickname":
                generateKey(1024)
                client.send(nickname.encode('ascii'))
                pass
            else:
                print(message)

        except:
            print("there's an error")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
