'''
Created on Apr 24, 2020

@author: RayL
'''
from pieces import Bishop,King,Queen,Pawn,Knight,Rook
import pygame

def setPawns(board):
    i = 1
    j = 0
    while j < len(board):
        board[i].append(Pawn(i,j,'black'))
        j += 1
    i = 6
    j = 0
    while j < len(board):
        board[i].append(Pawn(i,j,'white'))
        j += 1

def setPieces(board,p1,p2):
    for piece in p1: 
        board[0].append(piece)
    for piece in p2:
        board[7].append(piece)
        
class Board():
    
    def __init__(self,window):
        self.window = window
        self.spaceSize = 50
        self.blackRow = 0
        self.whiteRow = 7
        self.whiteKing = King(self.whiteRow,4,'white')
        self.blackKing = King(self.blackRow,4,'black')
        #Set up the board
        self.blackPieces =[Rook(self.blackRow,0,'black'), Knight(self.blackRow,1,'black'), 
             Bishop(self.blackRow,2,'black'), Queen(self.blackRow,3,'black'),
             self.blackKing, Bishop(self.blackRow,5,'black'), 
             Knight(self.blackRow,6,'black'), Rook(self.blackRow,self.whiteRow,'black')]
        
        self.whitePieces = [Rook(self.whiteRow,0,'white'), Knight(self.whiteRow,1,'white'), 
             Bishop(self.whiteRow,2,'white'), Queen(self.whiteRow,3,'white'),
             self.whiteKing, Bishop(self.whiteRow,5,'white'), 
             Knight(self.whiteRow,6,'white'), Rook(self.whiteRow,self.whiteRow,'white')]
        
        self.board = [
            [],
            [],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [],
            [] 
            ]
        setPawns(self.board)
        setPieces(self.board,self.blackPieces,self.whitePieces)
        dBoard = [x[:] for x in self.board]
        self.positions = [[dBoard,0]]
        
    def drawBoard(self):
        ###Draw Board###
        
        for row in range(len(self.board)):
            if row % 2 == 0:
                c = 0
            else:
                c = 1
            for col in range(len(self.board)):
                if c == 0:
                    pygame.draw.rect(self.window,
                                    (232,235,239),
                                    (col*self.spaceSize,row*self.spaceSize,
                                     self.spaceSize,self.spaceSize))
                    c = 1
                else:
                    pygame.draw.rect(self.window,
                                    (125,135,150),
                                    (col*self.spaceSize,row*self.spaceSize,
                                     self.spaceSize,self.spaceSize))
                    c = 0
    
    def move(self,piece,decision,dumBoard = None):
        ###Move the piece using a valid decision.###
        takes = False
        changed = False
        if dumBoard != None:
            board = dumBoard
        else:
            board = self.board
        row = decision[0]
        col = decision[1]
        rowOld = piece.row
        colOld = piece.col
        if board[row][col] != 0:
            takes = True
        if decision[-1] == 'CLong':
            board[row][col + 1] = Rook(row,col + 1, piece.color)
            board[row][0] = 0
        if decision[-1] == 'CShort':
            board[row][col - 1] = Rook(row,col - 1, piece.color)
            board[row][7] = 0
        board[row][col] = piece
        board[rowOld][colOld] = 0
        if dumBoard == None:
            piece.row = row
            piece.col = col
            dBoard = [x[:] for x in board]
            for b in self.positions:
                if dBoard == b[0]:
                    b[1] += 1
                    changed = True
                    if b[1] == 2:
                        return True
                    break
                changed = False
            if not changed:
                dBoard = [x[:] for x in board]
                self.positions.append([dBoard,0])
            if takes:
                dBoard = [x[:] for x in board]
                self.positions = [[dBoard,0]]
            if piece.isPawn: 
                dBoard = [x[:] for x in board]
                self.positions = [[dBoard,0]]
                piece.canMoveTwo = False
                if abs(row - rowOld) == 2: 
                    if row - 1 >= 0 and col + 1 <= 7 and row + 1 <= 7:
                        pPawn = board[row][col + 1]
                        if pPawn != 0:
                            if pPawn.isPawn and pPawn.color != piece.color:
                                if pPawn.color == 'black':
                                    pPawn.canEnPassant = [True,[row + 1,col]]
                                if pPawn.color == 'white':
                                    pPawn.canEnPassant = [True,[row -1,col]]
                    if row + 1 <= 7 and col - 1 >= 0 and row - 1 >= 0:
                        pPawn = board[row][col - 1]
                        if pPawn != 0:
                            if pPawn.isPawn and pPawn.color != piece.color:
                                if pPawn.color == 'black':
                                    pPawn.canEnPassant = [True,[row + 1,col]]
                                if pPawn.color == 'white':
                                    pPawn.canEnPassant = [True,[row -1,col]]
                if piece.canEnPassant[0]:
                    if piece.color == "white":
                        if board[piece.row + 1][piece.col] !=0 and board[piece.row + 1][piece.col].color != piece.color:
                            board[piece.row + 1][piece.col] = 0
                    else:
                        if board[piece.row - 1][piece.col] !=0 and board[piece.row - 1][piece.col].color != piece.color:
                            board[piece.row - 1][piece.col] = 0      
                if piece.row == 0 or piece.row == 7:
                    piece.promote(board,self.window) 
            if piece.isKing or piece.isRook: 
                piece.canCastle = False
    def drawPieces(self):
        ###Draw the pieces onto the board###

        for row in self.board:
            for piece in row:
                if piece != 0:
                    self.window.blit(piece.image,
                                    (piece.col*self.spaceSize,piece.row*self.spaceSize)
                                    )
    
                
        