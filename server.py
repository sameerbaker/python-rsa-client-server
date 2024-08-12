import threading
import socket
import pickle
import sys
"""0130011820235
سمير مصطفى بكر"""

from rsa import generateKey




host = "127.0.0.1"
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []




def broadcast(message):
    for client in clients:
        client.send(message)



def handling(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname}left the client  ! '.encode('ascii'))
            nicknames.remove(nickname)
            break





def receive():
    while True:

        client, address = server.accept()
        print(f"Connected with{str(address)}")

        client.send('nickname'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname} !')
        broadcast(f'{nickname}joined the chat '.encode('ascii'))
        client.send('connected to the chat '.encode('ascii'))

        thread = threading.Thread(target=handling, args=(client,))
        thread.start()


print("server is on....")

receive()