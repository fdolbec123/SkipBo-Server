import socket
import pickle

server = "192.168.100.195"
port = 5555
socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (server, port)
socket_de_connexion.connect(address)
msg = socket_de_connexion.recv(2048)
message = pickle.loads(msg)
print(message)
if message == "Connecté!":
    data_to_send = pickle.dumps("create")
    socket_de_connexion.send(data_to_send)
    code = socket_de_connexion.recv(2048)
    code_invitation = pickle.loads(code)
    print(code_invitation)
    player_info = {"username":"fdolbec123", "couleur":"bleu"}
    nbre_de_joueur = 2
    joueurs = pickle.dumps(((nbre_de_joueur), player_info))
    socket_de_connexion.send(joueurs)
    depart = socket_de_connexion.recv(2048)
    cartes_de_depart = pickle.loads(depart)
    print(cartes_de_depart)

