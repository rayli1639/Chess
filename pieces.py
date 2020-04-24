'''
Created on Apr 24, 2020

@author: RayL
'''

class Piece():
    
    def __init__(self,row,col,color):
        self.color = color
        self.row = row
        self.col = col
        self.isAlive = True
    
    def take(self,piece):
        ###Take the position of the other piece and destroy the piece###
        
        self.row = piece.row
        self.col = piece.col
        piece.isAlive = False
    

class Pawn(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self,row,col,color)
        
    def showSpaces(self):
        ###When this piece is selected, display possible moves###
        
        if self.color == 'black':
            space = [self.row + 1, self.col]
        else:
            space = [self.row - 1, self.col]
        return space
    
        
        
        


        
    
        
        
        