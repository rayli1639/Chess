'''
Created on May 4, 2020

@author: RayL
'''
import socket
from _thread import start_new_thread
import pickle
from board import Board
from board import create_FEN

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

s.listen()
print("waiting for Connection")

p1 = 'white'
p2 = 'black'
turn = 'white'
positions = [[create_FEN(board),0]]
drawCoords = []

def threaded_client(conn,p):
    
    global board
    global b
    global p1,p2
    global turn
    global positions
    global drawCoords
    global boardCreated
    
    start_info = pickle.dumps([p,b.whiteKing,b.blackKing])
    length = len(start_info).to_bytes(2, byteorder = 'big')
    conn.send(length + start_info)
    
    if p == p1:
        print('White Connected')
    elif p == p2:
        print('Black Connected')
    
#     if not boardCreated:
#         conn.send(str.encode('Waiting for Both Players to Connect'))
        
    while True:
        try:
            recv_data = b""
            i = 0
            while True:
                packet = conn.recv(4096)
                
                if i == 0:
                    size = int.from_bytes(packet[:2],byteorder = 'big')
                    packet = packet[2:]
                    i = 1
                recv_data += packet
                
                if len(recv_data) == size:
                    break
                
            data = pickle.loads(recv_data)
            
            if data[1] == 0:
                positions.append(data[0])
                
            elif data[1] == 1:
                positions = []
                positions.append(data[0])
                
            elif data[1] == 2:
                positions[data[2]][1] += 1   
                         
            elif type(data[0]) is list:
                ## Receive Information and change global var board
                board = data[0]
                drawCoords = data[1]
                
                if p == p1:
                    turn = 'black' ## Reply which player needs to move
                elif p == p2:
                    turn = 'white'
            
            if not data:
                print('Disconnected')
                break
            else:
                pass
#                 print('Received') ## Received Data
#                 print('Sending') ##Sending Reply
            dumped = pickle.dumps([board,turn,positions,drawCoords])
            length = len(dumped).to_bytes(2, byteorder = 'big')
#             print('Send Length: ' + str(len(dumped)))
            conn.sendall(length + dumped)
            
        except:
            break
        
    print('Lost Connection')
    conn.close()

p = 'white'

while True:
    conn,addr = s.accept()
    print('Connection to:', addr)
    start_new_thread(threaded_client,(conn, p))
    p = 'black'

