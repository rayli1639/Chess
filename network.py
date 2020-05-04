'''
Created on May 4, 2020

@author: RayL
'''

import socket

class Network():
    
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.187'
        self.port = 5555
        self.addr = (self.server,self.port)
        self.id = self.connect()
        print(self.id)
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    
    def send(self,data):
        try:
            self.client.send(str.encode(data)) ##Encode Data
            return self.client.recv(2048).decode() ##Decode and receive data
        except socket.error as e:
            print(e)

n = Network()
print(n.send('hello'))
print(n.send('working'))
