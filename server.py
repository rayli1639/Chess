'''
Created on May 4, 2020

@author: RayL
'''
import socket
from _thread import start_new_thread
import pickle
from board import Board

server = '192.168.1.187'
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    
b = Board()
board = b.board
boardCreated = False

s.listen(2)
print("waiting for Connection")

p1 = 'white'
p2 = 'black'
turn = 'white'
dBoard = [x[:] for x in board]
positions = [[dBoard,0]]

def threaded_client(conn,p):
    
    global board
    global b
    global p1,p2
    global turn
    global positions
    
    conn.send(pickle.dumps([p,b.whiteKing,b.blackKing]))
    
    if p == p1:
        print('You are white')
    elif p == p2:
        print('You are black')
        
    while True:
        try:
            data = pickle.loads(conn.recv(2048*32))
            
            if data[1] == 0:
                positions.append(data[0])
                print(positions)
            elif data[1] == 1:
                positions = []
                positions.append(data[0])
                print(positions)
            elif data[1] == 2:
                print(positions[data[2]][1])
                positions[data[2]][1] += 1
                print(positions)
                
            elif type(data[0]) is list:
                board = [x[:] for x in data[0]] ## Receive Information and change global var board
                
                if p == p1:
                    turn = 'black' ## Reply which player needs to move
                elif p == p2:
                    turn = 'white'
            
            if not data:
                print('Disconnected')
                break
            else:
                pass
#               print('Received') ## Received Data
#               print('Sending') ##Sending Reply
        except:
            break

        conn.sendall(pickle.dumps([board,turn,positions])) #Send Reply

    
    print('Lost Connection')
    conn.close()

idCount = 0

while True:
    conn,addr = s.accept()
    print('Connection to:', addr)
    if idCount == 0:
        start_new_thread(threaded_client,(conn, p1))
        idCount += 1
    elif idCount == 1:
        start_new_thread(threaded_client,(conn, p2))
        boardCreated = True
    
