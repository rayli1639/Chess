'''
Created on May 4, 2020

@author: RayL
'''

import socket
import pickle
import sys

class Network():
    
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.187'
        self.port = 5555
        self.addr = (self.server,self.port)
        self.info = self.connect()
    
    def getInfo(self):
        return self.info
    
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048)) #Receive Color
        except:
            pass
    
    def send(self,data):
        """
        :param data: board
        :param return: board
        """
        
        try:
            
            data = pickle.dumps(data)
            length = len(data).to_bytes(2,byteorder = 'big')
            self.client.send(length + data)
            
            recv_data = b""
            i = 0
            while True:
                packet = self.client.recv(4096)
                
                if i == 0:
                    size = int.from_bytes(packet[:2],byteorder = 'big')
                    packet = packet[2:]
                    i = 1
                recv_data += packet
                
                if len(recv_data) == size:
                    break

            return pickle.loads(recv_data) ##Decode and receive data
        
        except socket.error as e:
            print(e)


