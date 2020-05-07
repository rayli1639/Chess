'''
Created on May 4, 2020

@author: RayL
'''

import socket
import pickle

class Network():
    
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.187'
        self.port = 5555
        self.addr = (self.server,self.port)
        self.color = self.connect()
    
    def getColor(self):
        return self.color
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() #Receive Color
        except:
            pass
    
    def send(self,data):
        """
        :param data: board
        :param return: board
        """
        
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*8)) ##Decode and receive data
        except socket.error as e:
            print(e)


