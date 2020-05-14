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
            self.client.sendall(pickle.dumps('hello'))
            return pickle.loads(self.client.recv(2048)) #Receive Color
        except:
            pass
    
    def send(self,data):
        """
        :param data: board
        :param return: board
        """
        print(data)
        print(sys.getsizeof(data))
        try:
            self.client.sendall(pickle.dumps(data))
            print('data sent')
            recv_data = b""
            while True:
                packet = self.client.recv(4096)
                recv_data += packet
                if len(packet) < 4096:
                    break
                print('packet received')
            return pickle.loads(recv_data) ##Decode and receive data
        except socket.error as e:
            print(e)


