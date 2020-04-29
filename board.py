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
        if dumBoard != None:
            board = dumBoard
        else:
            board = self.board
        row = decision[0]
        col = decision[1]
        rowOld = piece.row
        colOld = piece.col
        board[rowOld][colOld] = 0
        board[row][col] = piece
        if dumBoard == None:
            piece.row = row
            piece.col = col
            if piece.isPawn: 
                piece.canMoveTwo = False
        
    def getBoard(self):
        ###Get the Board for Dummy Purposes###
        board = self.board.copy()
        return board
    
    def drawPieces(self):
        ###Draw the pieces onto the board###

        for row in self.board:
            for piece in row:
                if piece != 0:
                    self.window.blit(piece.image,
                                    (piece.col*self.spaceSize,piece.row*self.spaceSize)
                                    )
    
    def isKingChecked(self,king,dumBoard = None,s = None): 
        if dumBoard is not None:
            board = dumBoard
        else:
            board = self.board
        if s is None:
            s = [king.row,king.col]
        if king.color == 'white':
            for row in board:
                for piece in row:
                    if piece != 0:
                        if piece.color == 'black':
                            for space in piece.getSpaces(board):
                                if space[0] == s[0] and space[1] == s[1]:
                                    return True
        else:
            for row in board:
                for piece in row:
                    if piece != 0:
                        if piece.color == 'white':
                            for space in piece.getSpaces(board):
                                for space in piece.getSpaces(board):
                                    if space[0] == s[0] and space[1] == s[1]:
                                        return True
        return False
                
        