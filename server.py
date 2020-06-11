import socket
import pickle
import random
from _thread import *
games = {}
couleurs = ["Bleu", "Rouge", "Jaune", "Vert"]
paquet_de_carte_initial = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                           3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                           5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                           7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                           9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                           11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
                           12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
                           "SB", "SB", "SB", "SB", "SB", "SB", "SB", "SB", "SB", "SB", "SB", "SB"]
server = "192.168.100.195"
port = 5555
socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def code_invitation():
    print("")
    digit1 = random.choice('0123456789')  # Chooses a random element
    digit2 = random.choice('0123456789')
    digit3 = random.choice('0123456789')
    digit4 = random.choice('0123456789')
    code = digit1 + digit2 + digit3 + digit4
    games[code] = {}
    print(games)
    return code


def split_cards(nbre):
    print("in")
    random.shuffle(paquet_de_carte_initial)
    random.shuffle(paquet_de_carte_initial)
    random.shuffle(paquet_de_carte_initial)
    print(paquet_de_carte_initial)
    if nbre == 2:
        print(2)
        player0 = []
        player1 = []
        main0 = []
        main1 = []
        for i in range(30):
            player0.append(paquet_de_carte_initial[0])
            paquet_de_carte_initial.pop(0)
            player1.append(paquet_de_carte_initial[0])
            paquet_de_carte_initial.pop(0)
        # print(player0)
        # print(player1)
        for j in range(5):
            main0.append(paquet_de_carte_initial[0])
            paquet_de_carte_initial.pop(0)
            main1.append(paquet_de_carte_initial[0])
            paquet_de_carte_initial.pop(0)
        # print(main0)
        # print(main1)
        # print(paquet_de_carte_initial)
        setup = (player0, main0, player1, main1, paquet_de_carte_initial)
        return setup


try:
    socket_de_connexion.bind((server, port))
except socket.error as e:
    str(e)

socket_de_connexion.listen(4)
print("Le server a démaré. \n En attente d'une connexion...")
while True:
    conn, addr = socket_de_connexion.accept()
    print("Connecté à: ", addr)
    msg = pickle.dumps("Connecté!")
    conn.send(msg)
    while True:
        try:
            data_recu = conn.recv(2048)
            data = pickle.loads(data_recu)
            print(data)
            if data == "create":
                print("création d'un code d'invitation...")
                code_cree = code_invitation()
                print(code_cree)
                code_pickled = pickle.dumps(code_cree)
                conn.send(code_pickled)
                joueurs = conn.recv(2048)
                info_joueurs = pickle.loads(joueurs)
                print(info_joueurs)
                (nbre_de_joueurs, joueur0) = info_joueurs
                if nbre_de_joueurs == 2:
                    cle = str(code_cree)
                    # games[cle] = {"0": joueur0}
                    # test = games[cle]["0"]
                    setup = split_cards(nbre_de_joueurs)
                    (deck_joueur0, main_joueur0, deck_joueur1, main_joueur1, talon) = setup
                    joueur0['deck_joueur'] = deck_joueur0
                    joueur0['main_joueur'] = main_joueur0
                    print(joueur0)
                    joueur1 = {'username': '', 'couleur': ''}
                    joueur1['deck_joueur'] = deck_joueur1
                    joueur1['main_joueur'] = main_joueur0
                    joueur0['defausse0'] = []
                    joueur0['defausse1'] = []
                    joueur0['defausse2'] = []
                    joueur0['defausse3'] = []
                    joueur1['defausse0'] = []
                    joueur1['defausse1'] = []
                    joueur1['defausse2'] = []
                    joueur1['defausse3'] = []
                    joueur0['count'] = 30
                    joueur1['count'] = 30
                    # games[cle] = {"0": joueur0}
                    # games[cle] = {"1": joueur1}
                    games[cle] = {"talon": talon}
                    games[cle]['0'] = joueur0
                    games[cle]['1'] = joueur1
                    print(games[cle])
                    couleurs_restantes = couleurs
                    couleurs_restantes.remove(joueur0['couleur'])
                    print(couleurs_restantes)
                    test = games[cle]['1']['main_joueur']
                    print(len(test))
                    to_send_to_j0 = (games[cle]["talon"], games[cle]['0']['deck_joueur'], games[cle]['0']['main_joueur'], games[cle]['0']['count'], games[cle]['1']['deck_joueur'][0], len(test), games[cle]['1']['count'] )
                    print(to_send_to_j0)
                    depart = pickle.dumps(to_send_to_j0)
                    conn.send(depart)
            elif data == "join":
                print("in")
                ask = pickle.dumps("code?")
                conn.send(ask)
                code_recu_pickled = conn.recv(2048)
                code_recu = pickle.loads(code_recu_pickled)
                print(code_recu)
                verif = games.get(str(code_recu))
                if verif is not None:
                    print("yes")
                    reponse = pickle.dumps("Yes")
                    conn.send(reponse)
                else:
                    print("No")
                    reponse = pickle.dumps("No")
                    conn.send(reponse)
                    conn.close()

        except:
            break
    print("Connexion perdu")
    # conn.close()
