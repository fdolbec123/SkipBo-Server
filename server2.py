import socket
import pickle

HEADERSIZE = 10

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_de_connexion.bind((socket.gethostname(), 5555))
socket_de_connexion.listen(5)

while True:
    clientsocket, address = socket_de_connexion.accept()
    print(f"Connection from {address} has been established!")
    d = {1: "Test", 2: "Yay!"}
    msg = pickle.dumps(d)
    print(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(msg)