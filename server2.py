import socket
import select
import pickle

HEADERSIZE = 10

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_de_connexion.bind((socket.gethostname(), 5556))
# socket_de_connexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_de_connexion.listen(5)

# sockets_list = [socket_de_connexion]
#
# clients = {}
#
# # ---------------------------------------------------
#
#
# def receive_data(client_socket):
#     try:
#         data_header = client_socket.recv(HEADERSIZE)
#         if not len(data_header):
#             return False
#         data_length = int(data_header.decode("utf-8"))
#         return {"header": data_header, "data": client_socket.recv(data_length)}
#     except:
#         return False
#
#
# while True:
#     read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
#
#     for notified_socket in read_sockets:
#         if notified_socket == socket_de_connexion:
#             client_socket, client_address = socket_de_connexion.accept()
#             user = receive_data(client_socket)
#             if user is False:
#                 continue
#             sockets_list.append(client_socket)
#             clients[client_socket] = user
#             print(f"Nouvelle connexion de {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
#         else:
#             data = receive_data(notified_socket)
#             if data is False:
#                 print(f"Connexion fermée de {clients[notified_socket]['data'].decode('utf-8')}")
#                 sockets_list.remove(notified_socket)
#                 del clients[notified_socket]
#                 continue
#             user = clients[notified_socket]
#             print(f"Données provenant de {user['data'].decode('utf-8')}:{data['data'].decode('utf-8')}")
#
#             for client_socket in clients:
#                 if client_socket != notified_socket:
#                     socket_de_connexion.send(user['header'] + user['data'] + data['header'] + data['data'])
#
#     for notified_socket in exception_sockets:
#         sockets_list.remove(notified_socket)
#         del clients[notified_socket]

# --------------------------------------------------


while True:
    clientsocket, address = socket_de_connexion.accept()
    print(f"Connection from {address} has been established!")
    d = {1: "Test", 2: "Yay!"}
    msg = pickle.dumps(d)
    print(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(msg)
