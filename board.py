'''
Created on Apr 24, 2020

@author: RayL
'''

class Board():
    
    def __init__(self):
        self.board = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []  
            ]
    
    def hasPiece(self,row,col):
        ###Check if a coord on the board has a piece.###
        
        if self.board[row][col] != 0:
            return True
        return False
    
    def move(self,piece,decision):
        row = decision[0]
        col = decision[1]
        space = self.board[row,col]
        if self.board[decision[0],decision[1]] != 0:
            piece.take(space)
        else:
            piece.row = row
            piece.col = col
            
            
        