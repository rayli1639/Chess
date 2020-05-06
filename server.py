'''
Created on May 4, 2020

@author: RayL
'''
import socket
from _thread import start_new_thread
import pickle


server = '192.168.1.187'
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    
board = []
boardCreated = False

s.listen(2)
print("waiting for Connection")

p1 = 'white'
p2 = 'black'

def threaded_client(conn,board,p):
    global p1,p2
    
    conn.send(pickle.dumps(board))
    reply = 'hello'
    
    while True:
        try:
            data = pickle.loads(conn.recv(2048*8))
            for row in data:
                print(row)
            board = data ## Receive Information and change global var board
            
            if not data:
                print('Disconnected')
                break
            else:
                print('Received') ## Received Data
                print('Sending')
            
            conn.sendall(pickle.dumps(reply)) #Send Reply
        except: 
            break
        
    print('Lost Connection')
    conn.close()

idCount = 0

while True:
    conn,addr = s.accept()
    print('Connection to:', addr)
    if idCount == 0:
        start_new_thread(threaded_client,(conn,board,p1))
        idCount += 1
    elif idCount == 1:
        start_new_thread(threaded_client(conn, board, p2))
    
