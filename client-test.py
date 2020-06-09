import socket
import sys
import select
import  errno
import pickle

HEADERSIZE = 10

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_de_connexion.connect((socket.gethostname(), 5556))
# my_username = input("Username: ")
# socket_de_connexion.setblocking(False)
# username = my_username.encode("utf-8")
# username_header = f"{len(username):<{HEADERSIZE}}".encode("utf-8")
# socket_de_connexion.send(username_header + username)
#
# while True:
#     data = input(f"{my_username} > ")
#     if data:
#         data = data.encode("utf-8")
#         data_header = f"{len(data) :< {HEADERSIZE}}".encode("utf-8")
#         socket_de_connexion.send(data_header + data)
#     try:
#         while True:
#             username_header = socket_de_connexion.recv(HEADERSIZE)
#             if not len(username_header):
#                 print("Connexion fermée par le server")
#                 sys.exit()
#             username_length = int(username_header.decode("utf-8"))
#             username = socket_de_connexion.recv(username_length).decode("utf-8")
#             data_header = socket_de_connexion.recv(HEADERSIZE)
#             data_length = int(data_header.decode("utf-8"))
#             data = socket_de_connexion.recv(data_length).decode("utf-8")
#
#             print(f"{username} > {data}")
#     except IOError as e:
#         if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#             print("Reading error", str(e))
#             sys.exit()
#         continue
#
#     except Exception as  e:
#         print("General error", str(e))
#         sys.exit()
#
#
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
