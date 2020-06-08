import socket
import pickle
# from _thread import *
# import sys

test_data = {1: "Test", 2: "Autre test"}


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.100.195"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        a = True
        try:
            self.client.send(str.encode(data))
            while a:
                if self.client.recv(2048).decode() == "get":
                    self.client.send(str.encode("get"))
                else:
                    break
                    # if self.client.recv(2048).decode() == "stop":
                    # return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


n = Network()
# print(n.send("get"))
n.send("stop")
