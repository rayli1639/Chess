'''
Created on Apr 24, 2020

@author: RayL
'''
from pieces import Bishop,King,Queen,Pawn,Knight,Rook

class Board():
    
    def __init__(self):
        self.blackRow = 0
        self.whiteRow = 7
        self.board = [
            [Rook(0,self.blackRow,'black'), Bishop(self.blackRow,1,'black'), 
             Knight(self.blackRow,2,'black'), Queen(self.blackRow,3,'black'),
             King(self.blackRow,4,'black'), Bishop(self.blackRow,5,'black'), 
             Knight(self.blackRow,6,'black'), Rook(self.blackRow,self.whiteRow,'black')
             ],
            [],
            [],
            [],
            [],
            [],
            [],
            [Rook(self.whiteRow,0,'black'), Bishop(self.whiteRow,1,'black'), 
             Knight(self.whiteRow,2,'black'), Queen(self.whiteRow,3,'black'),
             King(self.whiteRow,4,'black'), Bishop(self.whiteRow,5,'black'), 
             Knight(self.whiteRow,6,'black'), Rook(self.whiteRow,self.whiteRow,'black')]  
            ]
        i = self.blackRow + 1
        j = 0
        while j < len(self.board) - 1:
            self.board[i].append(Pawn(i,j,'black'))
            j += 1
        i = self.whiteRow - 1
        j = 0
        while j < len(self.board) - 1:
            self.board[i].append(Pawn(i,j,'white'))
            j += 1
    
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
    
    def show(self):
        for i in range(0,len(self.board)):
            print(self.board[i])
            
board = Board()
board.show()
        