import socket
from _thread import *
# import pickle
# import sys

test_data2 = {1: "Test2", 2: "Autre test 2"}
server = "192.168.100.195"
port = 5555

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_de_connexion.bind((server, port))
except socket.error as e:
    str(e)

socket_de_connexion.listen(4)
print("Le server a démaré. \n En attente d'une connexion...")



def threaded_client(conn):
    i = 0
    conn.send(str.encode("Connecté!"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Déconnecté")
                break
            else:
                print("L'élément suivant a été reçu: ", reply)
                print("Envoi de l'élément suivant: ", reply)
            if data.decode("utf-8") == "get":
                pass
                # if i < 10:
                #     conn.sendall(str.encode(reply))
                #     i += 1
                #     print(i)
                # if i == 10:
                #     conn.sendall(str.encode("stop"))
                #     print("sending a stop signal")
            else:
                conn.sendall(str.encode(reply))
        except:
            break
    print("Connexion perdu")
    conn.close()


while True:
    conn, addr = socket_de_connexion.accept()
    print("Connecté à: ", addr)

    start_new_thread(threaded_client, (conn,))
