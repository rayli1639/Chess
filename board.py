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
        
class Board():
    
    def __init__(self,window):
        self.window = window
        self.spaceSize = 50
        self.blackRow = 0
        self.whiteRow = 7
        #Set up the board
        self.board = [
            [Rook(self.blackRow,0,'black'), Bishop(self.blackRow,1,'black'), 
             Knight(self.blackRow,2,'black'), Queen(self.blackRow,3,'black'),
             King(self.blackRow,4,'black'), Bishop(self.blackRow,5,'black'), 
             Knight(self.blackRow,6,'black'), Rook(self.blackRow,self.whiteRow,'black')
             ],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [Rook(self.whiteRow,0,'white'), Bishop(self.whiteRow,1,'white'), 
             Knight(self.whiteRow,2,'white'), Queen(self.whiteRow,3,'white'),
             King(self.whiteRow,4,'white'), Bishop(self.whiteRow,5,'white'), 
             Knight(self.whiteRow,6,'white'), Rook(self.whiteRow,self.whiteRow,'white')]  
            ]
        setPawns(self.board)
            
        #Draw the Board
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
        pygame.display.update()
        
    def hasPiece(self,row,col):
        ###Check if a coord on the board has a piece.###
        
        if self.board[row][col] != 0:
            return True
        return False
    
    def move(self,piece,decision):
        ###After a decision has been deemed valid, move the piece.###
        
        row = decision[0]
        col = decision[1]
        space = self.board[row,col]
        if self.board[decision[0],decision[1]] != 0:
            piece.take(space)
        else:
            piece.row = row
            piece.col = col
    
    def show(self):
        ###Show the array of the board###
        
        for i in range(0,len(self.board)):
            print(self.board[i])
    
    def drawPieces(self):
        ###Draw the pieces onto the board###
        
        for row in self.board:
            for piece in row:
                self.window.blit(piece.image,
                                (piece.col*self.spaceSize,piece.row*self.spaceSize)
                                )
        pygame.display.update()

        