'''
Created on May 4, 2020

@author: RayL
'''
import socket
from _thread import *
#import sys

server = '192.168.1.187'
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for Connection")

def threaded_client(conn):
    
    conn.send(str.encode('Connected'))
    reply = ''
    
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8') ## Receive Information and decode it.
            
            if not data:
                print('Disconnected')
                break
            else:
                print('Received: ' + reply) ## Received Data
                print('Sending: ' + reply)
            
            conn.sendall(str.encode(reply))
        except: 
            break
        
    print('Lost Connection')
    conn.close()

while True:
    conn,addr = s.accept()
    print('Connection to:', addr)
    start_new_thread(threaded_client,(conn,))
