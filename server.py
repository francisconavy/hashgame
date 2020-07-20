import socket
import time
from game_functions import *

#sockets configuration
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    print("Waiting for player 1 connection")
    clientsocket1, address1 = s.accept()
    print(f"Connection from {address1} has been established!")

    msg = "Welcome to the server!\nWaiting for player 2"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket1.send(msg)
    time.sleep(1)

    msg = "How to play:\nGive X and Y position\nExemple -> Player 1: 1 1"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket1.send(msg)
    time.sleep(1)

    print("Waiting for player 2 connection")
    clientsocket2, address2 = s.accept()
    print(f"Connection from {address2} has been established!")

    msg = "Welcome to the server!"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket2.send(msg)
    time.sleep(1)

    msg = "How to play:\nGive X and Y position\nExemple -> Player 2: 1 1"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket2.send(msg)
    time.sleep(1)
    
    msg = "The game will start"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket1.send(msg)
    time.sleep(1)

    msg = "The game will start"
    msg = pickle.dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket2.send(msg)
    time.sleep(1)

    start_game(clientsocket1, clientsocket2)
    if(input("Go to next game? y or n: ")=="n"):
        break
print("bye bye :)")