import socket
import pickle

HEADERSIZE = 10

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_de_connexion.connect((socket.gethostname(), 5555))

while True:
    full_msg = b""
    new_msg = True
    while True:
        msg = socket_de_connexion.recv(16)
        if new_msg:
            print(f"new message lenght: {msg[ :HEADERSIZE]}")
            msglen = int(msg[ :HEADERSIZE])
            new_msg = False
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("Full message received")
            print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b""

    print(full_msg)
